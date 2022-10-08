from logging import Logger
from shared.Utility import encode_varint, int_to_little_endian, little_endian_to_int, read_varint
from shared.Op import OP_CODE_FUNCTIONS, OP_CODE_NAMES

class Script:
    
    def __init__(self, cmds=None):
        if cmds is None:
            self.cmds = []
        else:
            self.cmds = cmds

    def __repr__(self):
        result = []
        for cmd in self.cmds:
            if type(cmd) == int:
                if OP_CODE_NAMES.get(cmd):
                    name = OP_CODE_NAMES.get(cmd)
                else:
                    name = 'OP_[{}]'.format(cmd)
                result.append(name)
            else:
                result.append(cmd.hex())
        return ' '.join(result)

    def __add__(self, other):
        return Script(self.cmds + other.cmds)

    def raw_serialize(self):
        result = b''
        for cmd in self.cmds:
            if type(cmd) == int:    #if this is an integer, cmd is an opcode
                result += int_to_little_endian(cmd, 1)
            else:
                length = len(cmd)
                if length < 75:     #if length is between 1 and 75, encode the length as a single byte
                    result += int_to_little_endian(length, 1)
                elif length > 75 and length < 0x100:
                    result += int_to_little_endian(76, 1)
                    result += int_to_little_endian(length, 1)
                elif length >= 0x100 and length <= 520:
                    result += int_to_little_endian(77, 1)
                    result += int_to_little_endian(length, 2)
                else:
                    raise ValueError('too long a command')
                result += cmd
        return result

    def serialize(self):
        result = self.raw_serialize()
        total = len(result)
        return encode_varint(total) + result
                
    def evaluate(self, z):
        cmds = self.cmds[:]     # copy commands list
        stack = []
        altstack = []
        while len(cmds) > 0:
            cmd = cmds.pop(0)
            if type(cmd) == int:
                operation = OP_CODE_FUNCTIONS[cmd]
                if cmd in (99, 100):                # 99 and 100 are OP_IF and OP_NOTIF
                    if not operation(stack, cmds):
                        Logger.info('bad op: {}'.format(OP_CODE_NAMES[cmd]))
                        return False
                elif cmd in (107, 108):            # OP_TOALTSTACK and OP_FROMALTSTACK
                    if not operation(stack, altstack):
                        Logger.info('bad op: {}'.format(OP_CODE_NAMES[cmd]))
                        return False
                elif cmd in (172, 173, 174, 175):  #OP_CHECKSIG, OP_CHECKSIGVERIFY, OP_CHECKMULTISIG, OP_CHECKMULTISIGVERIFY
                    if not operation(stack,z):
                        Logger.info('bad op: {}'.format(OP_CODE_NAMES[cmd]))
                        return False
                else:
                    if not operation(stack):
                        Logger.info('bad op: {}'.format(OP_CODE_NAMES[cmd]))
                        return False
            else:
                stack.append(cmd)
        if len(stack) == 0:
            return False
        if stack.pop() == b'':
            return False
        return True

    @classmethod
    def parse(cls, stream):
        script_length = read_varint(stream)
        cmds = []
        count = 0
        while count < script_length:
            current = stream.read(1)
            count += 1
            current_byte = current[0]
            if current_byte >= 1 and current_byte <= 75: # next n bytes are an element
                n = current_byte
                cmds.append(stream.read(n))
                count += n
            elif current_byte == 76:    # OP_PUSHDATA1 so the next byte tells us how many bytes to read
                data_length = little_endian_to_int(stream.read(1))
                cmds.append(stream.read(data_length))
                count += data_length + 1
            elif current_byte == 77:    # OP_PUSHDATA2 so the next 2 bytes tells us how many bytes to read
                data_length = little_endian_to_int(stream.read(2))
                cmds.append(stream.read(data_length))
                count += data_length + 2
            else:
                op_code = current_byte
                cmds.append(op_code)
        if count != script_length:
            raise SyntaxError('parsing script failed')
        return cls(cmds)
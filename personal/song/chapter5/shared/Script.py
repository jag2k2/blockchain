from shared.Utility import read_varint

class Script:
    
    @classmethod
    def parse(self, stream):
        script_length = read_varint(stream)
        contents = stream.read(script_length)[::-1]
        return contents.hex()
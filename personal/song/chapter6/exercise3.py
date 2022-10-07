from shared.Script import Script

if __name__ == '__main__':
    script_pubkey = Script([0x76, 0x76, 0x95, 0x93, 0x56, 0x87])
    script_sig = Script([0x52])
    combined_script = script_sig + script_pubkey
    print(combined_script.evaluate(0))
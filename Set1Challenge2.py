#write a function to XOR two hex strings together

def XOR(hex1string, hex2string):
    result = bytearray()
    #convert both hex strings into bytes
    hex1Bytes = bytes.fromhex(hex1string)
    hex2Bytes = bytes.fromhex(hex2string)
    #pairs bytes together for XOR
    test = zip(hex1Bytes, hex2Bytes)

    for byte1, byte2 in test:
        #XORs pairs
        result.append(byte1 ^ byte2)

    return result.hex()
        

XOR('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')




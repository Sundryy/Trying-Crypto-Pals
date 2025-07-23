
#convert hex to base64

# hex is below:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d


import base64

hexString = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

#converts hex into bytes
hexBytes = bytes.fromhex(hexString)

base64Bytes = base64.b64encode(hexBytes)

base64String = base64Bytes.decode('utf-8')




'''
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.


Find out the common letters

E T A O I N S H R D L U
'''


import base64

highestScore = 0

hexBytes = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

XORCharacter = bytearray(1)
highestCount = 0
possibleMessage = ''
possibleKey = ''


for i in range(256):

    XORCharacter[0] = i
    count = 0
    resultBytes = bytearray()

    for byte in hexBytes:



        XORResult = XORCharacter[0] ^ byte

        resultBytes.append(XORResult)


    plaintext = resultBytes.decode('utf-8', errors='ignore')


    for character in plaintext:
        if character.lower() in 'etaoinshrdlu ':
            count += 1
    
    if count > highestCount:
        highestCount = count
        possibleMessage = plaintext
        possibleKey = chr(i)



print(possibleMessage)
print(possibleKey)


'''
Message found: Cooking MC's like a pound of bacon
Character key: X

'''


    

        




#have to now XOR each byte and within each bit hold the score, the one with the highest score gets 
        


        
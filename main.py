import sys
import binascii
from KeyParser import KeyParser
from SDES import *
from ReadWriting import *

key ="11111111111"
flag1 = raw_input('Do you want to add new key(1) or default key(2) "1111111111"): ')
if (flag1 == '1'):
    key = raw_input('Enter you key: ')
    if (len(key)!=10):
        print("Invalid key")
        temp = raw_input("press any key")

flag2 = raw_input('Do you want to encrypt(1) or decrypt(2): ')
if(flag2 == '1'):
    #encryption
    plaintext = readFile("plaintext.txt")
    blockPlaintext = blockSeperate(plaintext)
    encryption = ""
    for i in blockPlaintext:
        encryption += Encryption(i, key)

    writeFile(encryption,"result_ciphertext.txt")
    print("Done!")
    raw_input("press any key")
else:
    #decryption
    ciphertext = readFile("result_ciphertext.txt")
    blockCiphertext = blockSeperate(ciphertext)
    decryption = ""
    for i in blockCiphertext:
        decryption +=Decryption(i, key)

    writeFile(decryption,"plaintext.txt")
    print("Done!")
    temp = raw_input("press any key")

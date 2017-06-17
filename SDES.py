from KeyParser import KeyParser

#divide into 2 halves
def TwoHalves(data):
    left = data[0:len(data)/2]
    right = data[len(data)/2:len(data)]
    return [left, right]

#X-OR bit
def Exclusive(a,b):
    y = int(a,2) ^ int(b,2)
    return '{0:0{1}b}'.format(y,len(a))

#inital permutation
def IP(data):
    ip = data[1] + data[5] + data[2] + data[0] + data[3] + data[7] + data[4] + data[6]
    return  ip

#inver IP
def inverseIP(data):
    inverseip= data[3] + data[0] + data[2] + data[4] + data[6] + data[1] + data[7] + data[5]
    return inverseip

#swap function
def SW(data):
    sw = TwoHalves(data)
    return sw[1]+sw[0]

def fX(left, right, key):
    e_p = right[3] + right[0] + right[1] + right[2] + right[1] + right[2] + right[3] + right[0]
    exc = Exclusive(e_p, key)
    S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    vS0 = S0[int(exc[0]+ exc[3], 2)][int(exc[1]+ exc[2], 2)]
    vS1 = S1[int(exc[4]+ exc[7], 2)][int(exc[5]+ exc[6], 2)]

    bS0 = '{0:0{1}b}'.format(vS0, 2)
    bS1 = '{0:0{1}b}'.format(vS1, 2)

    p4 = bS0[1] + bS1[1] +bS1[0] + bS0[0]

    excP4 = Exclusive(p4, left)
    return excP4 + right

def SDES(text, key1, key2):
    p10 = IP(text)
    ar1 = TwoHalves(p10)
    fx1 = fX(ar1[0], ar1[1], key1)

    fSW = SW(fx1)
    ar2 = TwoHalves(fSW)
    fx2 = fX(ar2[0], ar2[1], key2)

    result = inverseIP(fx2)
    return result

#encryption plaintext , key
def Encryption(plaintext, key):
    key = KeyParser(key)
    ciphertext = SDES(plaintext, key.getK1(), key.getK2())
    return ciphertext

#decryption plaintext , key
def Decryption(ciphertext, key):
    key = KeyParser(key)
    plaintext = SDES(ciphertext, key.getK2(), key.getK1())
    return plaintext


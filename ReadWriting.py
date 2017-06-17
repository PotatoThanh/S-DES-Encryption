import binascii

#seperate bin string into 8bit in 1cell array
def blockSeperate(bin):
    result = []
    for i in range(0, len(bin), 8):
        result.append(bin[i:i+8])
    return result

#readfile into bin string
def readFile(filename, mode='r'):
    f = open(filename, mode)
    result = text_to_bits(f.read())
    f.close()
    return result

#writefile from bin string input
def writeFile(bin, filename, mode='w'):
    contain = text_from_bits( bin)
    #contain = bin
    f = open(filename, mode)
    f.write(contain)
    f.close()
    return;


def text_to_bits(text):
    result = ""
    for i in text:
        t = ord(i)
        result += '{0:0{1}b}'.format(t,8)
    return result

def text_from_bits(bits):
    block = blockSeperate(bits)
    result = ""
    for i in block:
        result += chr(int(i, 2))
    return result

# 0101010001010100
# print(text_from_bits("0101010001010100"))
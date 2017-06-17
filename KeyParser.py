class KeyParser:
    __key = []
    def __init__(self, key):
        KeyParser.__key = KeyParser.KeyGenerate(key)

    def getK1(self):
        return self.__key[0]

    def getK2(self):
        return self.__key[1]

    @staticmethod
    def KeyP10(key):
        keyP10 = key[2] + key[4] + key[1] + key[6] + key[3] + key[9] + key[0] + key[8] + key[7] + key[5];
        return keyP10

    @staticmethod
    def KeyP8(key):
        keyP8 = key[5] + key[2] + key[6] + key[3] + key[7] + key[4] + key[9] + key[8];
        return keyP8

    @staticmethod
    def CLS(data,offset):
        result = ""
        for iter in range(0,offset):
            result = data[1:len(data)]
            result += data[0]
            data = result
        return result

    @staticmethod
    def KeyGenerate(key):
        keyP10 = KeyParser.KeyP10(key)
        cls1 = KeyParser.CLS(keyP10[0:len(keyP10)/2],1) + KeyParser.CLS(keyP10[len(keyP10)/2:len(keyP10)],1)
        key1 = KeyParser.KeyP8(cls1)

        cls2 = KeyParser.CLS(cls1[0:len(cls1)/2],2) + KeyParser.CLS(cls1[len(cls1)/2:len(cls1)],2)
        key2 = KeyParser.KeyP8(cls2)
        return [key1, key2]

class Hero :

    def __init__(self,inputName,inputHealth,inputPower):
        self.__name=inputName
        self.__health=inputHealth
        self.__power=inputPower
    #getter
    def getname(self):
        return self.__name

    def gethealth(self):
        print("darah " + self.__name + " adalah " )
        return self.__health

    #setter
    def serangan(self,serang):
        self.__health -= serang
        print("serangan terasa " + str(serang))
        print("darah " + self.__name + " menjadi " + str(self.__health))

earthshaker = Hero("earthshaker",100,25)

print(earthshaker.gethealth())
earthshaker.serangan(5)
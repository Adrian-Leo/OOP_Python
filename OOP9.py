class Hero :
    __jumlah = 0

    def __init__(self,inputName):
        self.__name=inputName
        Hero.__jumlah += 1

    #hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah
    #hanya berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    #method static (decorator) nempel ke objek dan class

    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


sniper = Hero("sniper")
print(sniper.getJumlah())
print(Hero.getJumlah1())
rikimaru = Hero("rikimaru")
print(rikimaru.getJumlah2())
print(Hero.getJumlah2())
rikimaru = Hero.getJumlah2()
print(rikimaru)
akai=Hero("akai")

print(akai.getJumlah3())
print(Hero.getJumlah3())



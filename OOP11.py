class Hero :
    __jumlah = 0

    def __init__(self,inputName,inputHealth,inputAttPower,inputArmor):
        self.__name = inputName
        self.__healthStandart = inputHealth
        self.__attPowerStandart = inputAttPower
        self.__armorStandart = inputArmor
        self.__level = 1
        self.__exp=0

        self.__healthMax = self.__healthStandart * self.__level
        self.__attPower= self.__attPowerStandart * self.__level
        self.__armor = self.__armorStandart * self.__level

        self.__health = self.__healthStandart

    @property
    def info(self):
        return "{} level {} : \n\t health : {} / {} \n\t attPower : {} \n\t armor : {}".format(self.__name,self.__level,self.__health, self.__healthMax,self.__attPower,self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        maxExp = 100
        maxExp += 10
        if(maxExp<=200) :
            if (self.__exp >= maxExp):
                print(self.__name, "level up")
                self.__level += 1
                self.__exp -= 100

                self.__healthMax = self.__healthStandart * self.__level
                self.__attPower = self.__attPowerStandart * self.__level
                self.__armor = self.__armorStandart * self.__level
        else :
            print("you have reaching maximum level")




    def attack(self,lawan):
        self.gainExp = 50




sven = Hero("sven ",100,25,10)
sniper = Hero("sniper ", 125,20,15)

print(sven.info)
sven.attack(sniper)
sven.attack(sniper)
print(sven.info)
sven.attack(sniper)
sven.attack(sniper)
print(sven.info)
print(sven.__dict__)

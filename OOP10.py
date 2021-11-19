class Hero :
    def __init__(self,inputName,inputHealth,inputArmor):
        self.name=inputName
        self.__health=inputHealth
        self.__armor=inputArmor
        #bentuk static variable
        # self.info = "Name : {} \n health : {} ".format(self.name,self.__health)

    #lebih dinamis
    @property
    def info(self):
        return "Name : {} \n health : {} ".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    #merubah variable armor dengan paradigma method
    @armor.setter
    def armor(self,input):
        self.__armor = input

    #untuk delete variable pada init

    @armor.deleter
    def armor(self):
        print("armor di delete ")
        self.__armor = None


sniper = Hero("sniper",100,15)
# print(sniper.info)

#merubah variable name
print(sniper.info)
sniper.name="dadang"
print(sniper.info)

print("getter dan setter")
print(sniper.armor)
print(sniper.__dict__)
sniper.armor=30
print(sniper.armor)
print(sniper.__dict__)

#delete armor

del sniper.armor
print(sniper.__dict__)
print(sniper.armor)

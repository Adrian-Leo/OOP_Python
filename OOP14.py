class Hero :
    def __init__(self,inputName,inputHealth):
        self.name=inputName
        self.health=inputHealth

    def showInfo(self):
        print("{} \n\t health {}".format(self.name,self.health))

class Hero_intelligent(Hero) :
    def __init__(self,name):
        super().__init__(name,150)


    def showInfo(self):
        print("ini subclass hero intelligent")
        print("{} \n\t tipe : intelligence \n\t health : {} ".format(self.name,self.health))


class Hero_tank(Hero):
    def __init__(self,name):
        super().__init__(name, 150)

    def showInfo(self):
        print("ini subclass hero tank")
        print("{} \n\t tipe : tank \n\t health : {} ".format(self.name,self.health))



saber = Hero_intelligent("saber")
akai = Hero_tank("akai")

print("")
saber.showInfo()
print(" ")
akai.showInfo()
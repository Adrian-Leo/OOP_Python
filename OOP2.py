class heroes :
    def __init__(self,inputName,inputHealth,inputPower,inputArmor): #CONSTRUCTOR
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = heroes("sniper",100,20,50)
hero2 = heroes ("mirana",200,10,25)
hero3 = heroes ("akai",350,5,50)

print(hero1.__dict__)
print(hero1.name)
print(hero2.__dict__)
print(hero3.__dict__)
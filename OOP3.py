class heroes :
    jumlah = 0 # INSTANCE CLASS / ATTRIBUTE CLASS
    def __init__(self,inputName,inputHealth,inputPower,inputArmor): #CONSTRUCTOR
        self.name = inputName # INSTANCE VARIABLE / ATTRIBUTE VARIABLE
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroes.jumlah += 1
        print("membuat hero dengan nama " + inputName)

hero1 = heroes("sniper",100,20,50)
print(heroes.jumlah)
hero2 = heroes ("mirana",200,10,25)
print(heroes.jumlah)
hero3 = heroes ("akai",350,5,50)
print(heroes.jumlah)




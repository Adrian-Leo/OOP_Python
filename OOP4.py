class heroes :
    jumlah = 0 # INSTANCE CLASS / ATTRIBUTE CLASS
    def __init__(self,inputName,inputHealth,inputPower,inputArmor): #CONSTRUCTOR
        self.name = inputName # INSTANCE VARIABLE / ATTRIBUTE VARIABLE
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        heroes.jumlah += 1


    # void function / method tanpa nilai kembali
    def hrName(self):
        print(" namaku adalah " + self.name)

    #method dengan argumen
    def healthUp(self,x):
        self.health += x

    #methode dengan return
    def getHealth(self):
        return self.health

hero1 = heroes("sniper",100,20,50)  
hero2 = heroes ("mirana",200,10,25)
hero3 = heroes ("akai",350,5,50)

hero1.hrName()
hero2.healthUp(20)
print("darah mirana bertambah menjadi" ,hero2.health)
hero3.healthUp(10)
print("darah akai bertambah menjadi", hero3.getHealth())

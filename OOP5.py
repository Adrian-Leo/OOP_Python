class hero :
    def __init__(self,inputName,inputHealth,inputAttack, inputArmor):
        self.name=inputName
        self.health=inputHealth
        self.attack =inputAttack
        self.armor=inputArmor

    def serang(self,lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self,self.attack)

    def diserang(self,lawan2,attack_lawan):
        print(self.name + " diserang " + lawan2.name)
        attack_diterima = attack_lawan / self.armor
        print("serangan terasa " + str(attack_diterima) )
        self.health -= attack_diterima
        print("darah " + self.name + " menjadi : " + str(self.health))

#INI CARA MASUKIN INPUT KE CLASS
sniper = hero("sniper",100,20,10)
sven = hero("sven",70,40,20)

sniper.serang(sven)
print("-" * 30)
sven.serang(sniper)
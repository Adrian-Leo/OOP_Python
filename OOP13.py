class Hero:
    def __init__(self,inputName,inputHealth):
        self.name=inputName
        self.health=inputHealth

    def info(self):
        print("{} dengan health : {}".format(self.name,self.health))

class Hero_tank(Hero): #ini adalah subclass
    def __init__(self,name):
        #Hero.__init__(self,name,200) alternatif 1
        #alternatif 2
        super().__init__(name,200)
        super().info()

class Hero_marksman(Hero): # ini adalah subclass
    def __init__(self,name):
        #Hero.__init__(self,name,100)alternatif 1
        # alternatif 2
        super().__init__(name,100)
        super().info()



akai =Hero_tank("akai")
miya = Hero_marksman("miya")

# print(akai.name , " ",akai.health) alternatif 1

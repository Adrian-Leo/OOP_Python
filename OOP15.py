class HERO :
    def __init__(self,inputName):
        self.__name=inputName
        self.health_pool=[0,100,120,140,160,180]
        self.attPower_pool=[0,20,40,60,80,100]
        self.armor_pool=[0,1,2,3,4,5]
        self.__level=0
        self.__exp=0

    def show_info(self):
        print("name :  {}\n\t level : {} \n\t health : {} \n\t attPower : {} \n\t armor: {} \n\t".format(
            self.__name,
            self.__level,
            self.__health,
            self.__attPower,
            self.__armor
        )
    )

    @property
    def health_pool(self):
        pass

    @property
    def attPower_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @health_pool.setter
    def health_pool(self, input):
        self.__health_pool = input

    @attPower_pool.setter
    def attPower_pool(self,input):
        self.__attPower_pool=input

    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool = input

    @levelUp.setter
    def levelUp(self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]

    @gainExp.setter
    def gainExp(self,input):
        self.__exp += input
        if (self.__exp>=100):
            self.levelUp = self.__exp//100
            self.__exp %= 100

    def attack(self):
        self.gainExp =50


class Hero_tank(HERO):
    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,50,100,150,200,250]
        self.attPower_pool =[0,20,40,60,80,100]
        self.armor_pool= [0,5,10,15,20,25]
        self.levelUp=1



class Hero_marksman(HERO):
    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0, 25, 50, 100, 125, 150]
        self.attPower_pool = [0, 30, 50, 70, 90, 110]
        self.armor_pool = [0, 5, 10, 15, 20, 25]
        self.levelUp = 1















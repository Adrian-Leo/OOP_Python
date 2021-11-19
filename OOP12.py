class Hero :

    def __init__(self,inputName,inputHealth):
        self.__name=inputName
        self.__health=inputHealth

class Hero_tank(Hero) :
    pass

class Hero_marksman(Hero) :
    pass

akai = Hero("akai",100)
tigreal = Hero_tank("tigreal",50)
print(tigreal.__dict__)
miya = Hero_marksman("miya",25)
print(miya.__dict__)



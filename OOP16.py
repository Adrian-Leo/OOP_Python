class Team :
    def hero_team(self,inputTeam):
        self.team = inputTeam

    def show_team(self):
        print(self.team)

class Tipe :

    def hero_tipe(self,inputTipe):
        self.tipe=inputTipe

    def show_tipe(self):

        print(self.tipe)


class Hero(Team,Tipe) :
    def __init__(self,inputName,inputHealth):
        self.name = inputName
        self.health = inputHealth

    def show_info(self):
        print("{} \n\t health : {}".format(self.name,self.health))

akai=Hero("akai",100)
akai.show_info()
print(30*"-")

akai.hero_team("biru")
akai.show_team()
print(30*"-")

akai.hero_tipe("tank")
akai.show_tipe()
print(30*"-")
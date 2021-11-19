class hero:
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,inputName,inputHealth):
        self.name=inputName
        self.health =inputHealth

        #tidak dapat diakses
        self.__private= "private"

        #dapat diakses sama seperti public
        self._protected="protected"

akai=hero("akai",150)
print(akai.__dict__)
akai._protected = "testing"
# akai.__private = "testing 2" --> tidak dapat dirubah
print(akai.__dict__)
print(akai._protected)
print(hero.__dict__)
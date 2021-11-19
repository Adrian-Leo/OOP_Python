class Mangga:
    def __init__(self,nama,jumlah):
        self.name=nama
        self.quantity=jumlah

    def __repr__(self):
        return "debug : mangga : {}  jumlah : {} ".format(self.name,self.quantity)

    def __str__(self):
        return "mangga : {}  jumlah : {} ".format(self.name,self.quantity)

    def __add__(self, objek):
        return self.quantity + objek.quantity


belanja1 = Mangga("arumanis",10)
belanja2=Mangga("ambon",15)
print(belanja1)
print(repr(belanja1))

print("jumlah hasil belanja : ",belanja1 + belanja2)


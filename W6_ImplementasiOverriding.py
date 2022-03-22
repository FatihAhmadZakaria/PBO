class Segiempat():
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitungluas(self): # Method Overriding
        print("Luas Segiempat = ", self.panjang * self.lebar, "m^2")

class Bujursangkar(Segiempat):
    def __init__(self, sisi):
        self.sisi = sisi
        Segiempat.__init__(self, sisi, sisi)

    def hitungluas(self): # Method Overriding
        print("Luas Bujur Sangkar = ", self.sisi * self.sisi, "m^2")

b = Bujursangkar(4)
s = Segiempat(2,4)
b.hitungluas()
s.hitungluas()
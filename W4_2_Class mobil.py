#Semua variabel bersifat public
class Mobil():
    def __init__(self, jendela, pintu, mesin):
        self.jendela = jendela
        self.pintu = pintu
        self.mesin = mesin

audi=Mobil(4,5,"Diesel")
print(audi.jendela)
print(audi.pintu)
print(audi.mesin)
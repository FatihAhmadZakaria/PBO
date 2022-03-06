#Semua variabel bersifat private
class Mobil():
    def __init__(self,jendela,pintu,mesin):
        self.__jendela=jendela
        self.__pintu=pintu
        self.__mesin=mesin

audi=Mobil(4,4,"Diesel")
print(audi._Mobil__mesin)
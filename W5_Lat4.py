# Multiple Inheritance

#Parent 1
class Perhitungan1:
    def penjumlahan(self,a,b):
        return a+b

#Parent 2
class Perhitungan2:
    def perkalian(self,a,b):
        return a*b

#Child
class Hitung(Perhitungan1, Perhitungan2):
    def pembagian(self,a,b):
        return a/b

h=Hitung()
print(h.penjumlahan(20,30))
print(h.perkalian(5,4))
print(h.pembagian(6,12))
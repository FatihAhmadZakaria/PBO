class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

segitiga_besar = Segitiga(100,80)

#akses variabel public: alas, tinggi, dan Luas dair Luar kelas Segitiga
print("alas: ",segitiga_besar.alas)
print("tinggi: ",segitiga_besar.tinggi)
print("luas: ",segitiga_besar.luas)
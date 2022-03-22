# Implementasi Overloading

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        #self.prodi = prodi
        #self.thn_masuk = thn_masuk
        #self.semester = semester

    def tampilMhs(self):
        print("Nama : ", self.nama, ", nim : ", self.nim)

    # Overloading Method
    def hitungSKS(self, jmlsks=None, sks=None):
        if jmlsks != None and sks != None:
            totalsks = jmlsks+sks
            print("Total SKS = ", totalsks)
        else:
            totalsks = jmlsks
            print("Total SKS = ", totalsks)

# Memanggil kelas
mhs1 = Mahasiswa("Eren", 123180015)
mhs2 = Mahasiswa("Luffy", 123190007)
mhs1.tampilMhs()
mhs2.tampilMhs()
mhs1.hitungSKS(80, 34) # Overloading
mhs2.hitungSKS(83) # Overloading
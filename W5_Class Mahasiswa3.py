# Hierarchical Inheritance

class Mahasiswa():
    def __init__(self,nama,nim):
        self.nama=nama
        self.nim=nim

class Siswa1 (Mahasiswa):
    def __init__ (self, nama,nim):
        self.nama=nama
        self.nim=nim

    def detSiswa1(self):
        print (self.nama,'alamat: wall rose')

class Siswa2(Siswa1):
    def __init__(self,nama, nim):
        self.nama=nama
        self.nim=nim

    def detSiswa2(self):
        print (self.nama,'jurusan: Informatika')

mhs1=Siswa1('Mikasa',135105)
mhs2=Siswa2('Nezuko',135117)

print(mhs1.nim)
mhs1.detSiswa1()
print(mhs2.nim)
mhs2.detSiswa2()
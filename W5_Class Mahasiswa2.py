# Multilevel Inheritance

class Mahasiswa():
    def __init__(self,nama,nim):
        self.nama=nama
        self.nim=nim

class Siswa1 (Mahasiswa):
    def __init__ (self, nama,nim):
        self.nama=nama
        self.nim=nim

class Siswa2(Siswa1):
    def __init__(self,nama, nim):
        self.nama=nama
        self.nim=nim

mhs1=Mahasiswa('Mikasa', 135105)
mhs2=Siswa1('Nezuko',135117)
mhs3=Siswa2('Hancock',134079)

print(mhs1.nama, mhs1.nim)
print(mhs2.nim)
print(mhs3.nama)
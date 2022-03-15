# Multiple Inheritance

class Mahasiswa1():
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

class Mahasiswa2():
    def __init__(self,alamat,jurusan):
        self.alamat = alamat
        self.jurusan = jurusan

class Siswa(Mahasiswa1,Mahasiswa2):
    def __init__(self, nama, nim, alamat, jurusan):
        Mahasiswa1.__init__(self, nama, nim)
        Mahasiswa2.__init__(self,alamat,jurusan)

s=Siswa('Mikasa',135105,'wall rose','Informatika')
print('nim:',s.nim, 'nama:',s.nama, 'alamat:',s.alamat, 'jurusan:',s.jurusan)
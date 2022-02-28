class Buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku = Buku('Tenggelamnya Kapal Van der Wick','HAMKA',1938)
t = 'Buku {} karanga {} pertama kali diterbitkan tahun {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit)
print(t)
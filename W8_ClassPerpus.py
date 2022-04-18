class PerpusItem:
    def __init__(self,judul,subjek,lokasi,info):
        self.judul = judul
        self.subjek = subjek
        self.lokasi = lokasi
        self.info = info
'''def lokasiSinpan(self):
    self.lokasi = lokasi
    self.info = info'''
class Buku(PerpusItem):
    def __init__(self,judul,subjek,lokasi,info,isbn,pengarang,jmlhal,ukuran):
        super().__init__(judul,'Buku',lokasi,info)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal
        self.ukuran = ukuran

class Majalah(PerpusItem):
    def __init__(self,judul,subjek,lokasi,info,volume,issue):
        super().__init__(judul,'Majalah',lokasi,info)
        self.volume = volume
        self.issue = issue

class DVD(PerpusItem):
    def __init__(self,judul,subjek,lokasi,info,aktor,genre):
        super().__init__(judul,'DVD',lokasi,info)
        self.aktor = aktor
        self.genre = genre

b = Buku('Pemrograman Python','Buku Cetak','Rak nomor 1','dipinjam','945-884-98-02','Yogi Syarif',2,'25x15')
m = Majalah('Dunia komputer','Majalah cetak','Rak nomor 2','ada','VII','komputer')
d = DVD('Shingeki no kyojin','sofcopy','Rak nomor 3','ada','Mikasa','Anime')
daftar = [b,m,d]
for dft in daftar:
    print('{} {} {}'.format(dft.judul,dft.subjek,dft.lokasi,dft.info))


class Buku:
    def __init__(self,judul,pengarang,tahun_terbit,tipe,penerbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.tipe = tipe
        self.penerbit = penerbit

buku1 = Buku('Tenggelamnya Kapal Van der Wick','HAMKA',1938,'Novel','Centrale Courant')
buku2 = Buku('Orang Orang Biasa','Andrea Hirata',2019,'Novel','Bentang Pustaka')
buku3 = Buku('Bedebah Di Ujing Tanduk','Tere Liye',2021,'Novel','Sabak Grib')
buku4 = Buku('Negeri 5 Menara','Ahmad Fuadi',2009,'Novel','Gramedia')
buku5 = Buku('Madilog','Tat Malaka',1943,'Filsafat','Narasi')
pilihan_buku = [buku1,buku2,buku3,buku4,buku5]
print('Daftar Buku')
for buku in pilihan_buku:
    t = 'Buku {} {} karangan {} pertama kali diterbitkan tahun {} Penerbit {}'.format(buku.tipe,buku.judul,buku.pengarang,buku.tahun_terbit,buku.penerbit)
    print(t)
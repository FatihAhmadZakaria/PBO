class MenuMinuman:
    def __init__(self,nama,deskripsi,harga,jenis,tipe,stok):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.jenis = jenis
        self.tipe = tipe
        self.__stok = stok

mnm1 = MenuMinuman('Jus Jambu','Jus Jambu Merah tanpa gula',8500,'Spesial','Dingin',12)
mnm2 = MenuMinuman('Jes Alpukat Ori','Jus Alpukat dengan tambahan air gula merah',15000,'Spesial','Dingin',32)
mnm3 = MenuMinuman('Jus Alpukat Xtra Milk','Jus Alpukat dengan campuran susu cokelat dan taburan kepingan choco',15000,'Spesial','Dingin',11)
mnm4 = MenuMinuman('Teh Manis','Teh Manis',2000,'Biasa','Hangat',4)
mnm5 = MenuMinuman('Kopi Ice','Kopi dengan gula dan tambahan ice',6000,'Spesial','Dingin',13)
mnm6 = MenuMinuman('Kopi Hitam','Kopi Hitam dengan sedikit gula',4000,'Spesial','Panas',52)

pilihan_minuman = [mnm1,mnm2,mnm3,mnm4,mnm5,mnm6]
print('Daftar Menu Minuman')
for mn in pilihan_minuman:
    t = '{} harga Rp {}, {}, {}, {} stok tersedia {}'.format(mn.nama,mn.harga,mn.deskripsi,mn.jenis,mn.tipe,mn._MenuMinuman__stok)
    print(t)
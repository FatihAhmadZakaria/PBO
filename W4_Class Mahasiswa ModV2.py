class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk,umur,kelas,asal):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.umur = umur
        self.kelas = kelas
        self.__asal = asal

m1 = Mahasiswa('Udin','10120371','Sistem Informasi',2020,19,'A','Jakarta')
m2 = Mahasiswa('Franklin','10130372','Sistem Komputer',2019,20,'B','Jambi')
m3 = Mahasiswa('Carl','10153164','Akutansi',2017,19,'F','Bekasi')
m4 = Mahasiswa('Michel','10160946','Hukum',2021,20,'D','Kalimantan')
m5 = Mahasiswa('Trevor','10170653','Farmasi',2020,22,'G','Lampung')
pilihan_mahasiswa = [m1,m2,m3,m4,m5]
print('Daftar Mahasiswa')
for m in pilihan_mahasiswa:
    teks = '{} adalah Mahasiswa {} angkatan {} dengan nim {} berumur {} kelas {} asal {}'.format(m.nama,m.prodi,m.thn_masuk,m.nim,m.umur,m.kelas,m._Mahasiswa__asal)
    print(teks)
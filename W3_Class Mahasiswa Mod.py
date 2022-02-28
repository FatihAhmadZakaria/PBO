class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk,umur,kelas):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.umur = umur
        self.kelas = kelas

m1 = Mahasiswa('Udin','10120371','Sistem Informasi',2020,19,'A')
m2 = Mahasiswa('Franklin','10130372','Sistem Komputer',2019,20,'B')
m3 = Mahasiswa('Carl','10153164','Akutansi',2017,19,'F')
m4 = Mahasiswa('Michel','10160946','Hukum',2021,20,'D')
m5 = Mahasiswa('Trevor','10170653','Farmasi',2020,22,'G')
pilihan_mahasiswa = [m1,m2,m3,m4,m5]
print('Daftar Mahasiswa')
for m in pilihan_mahasiswa:
    teks = '{} adalah Mahasiswa {} angkatan {} dengan nim {} berumur {} kelas {}'.format(m.nama,m.prodi,m.thn_masuk,m.nim,m.umur,m.kelas)
    print(teks)
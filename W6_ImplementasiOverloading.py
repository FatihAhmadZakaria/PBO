# Implementasi Overloading

class Pegawai:
    jumlah = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Pegawai.jumlah += 1

    def tampilJumlah(self):
        print("Total pegawai ", Pegawai.jumlah)

    def tampilPegawai(self):
        print("Nama : ", self.nama, ", gaji : ", self.gaji)

    #Method Overloading
    def tunjangan(self, istri=None, anak=None):
        if anak != None and istri != None:
            total = anak + istri
            print("Tunjangan anak + istri = ", total)
        else:
            total = istri
            print("Tunjangan istri = ", total)

# Memanggil Kelas
peg1 = Pegawai("Eren", 2000)
peg2 = Pegawai("Luffy", 6000)
peg1.tampilPegawai()
peg2.tampilPegawai()
peg1.tunjangan(2500, 2000)  #Overloading
peg2.tunjangan(2500)        #Overloading

print("Total pegawai %d" % Pegawai.jumlah)
rataGaji=(peg1.gaji + peg2.gaji)/Pegawai.jumlah
print("Rata-rata gaji = "+str(rataGaji))
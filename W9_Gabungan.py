# Implementasi Overloading
import math
class Gaji:
    def __init__(self, gaji_bulanan):
        self.gaji_bulanan = gaji_bulanan

    def total(self):
        return (self.gaji_bulanan*12)

class Pegawai:
    jumlah = 0

    def __init__(self, nama, gaji_bulanan, bonus):
        self.nama = nama
        self.gaji_bulanan = gaji_bulanan
        self.bonus = bonus
        self.obj_gaji = Gaji(self.gaji_bulanan)
        Pegawai.jumlah += 1

    def hasil_tahunan(self):
        return "Total gaji tahunan: "+ str(self.obj_gaji.total() + self.bonus) + ' Rupiah'

    def tampilJumlah(self):
        print("Total pegawai ", Pegawai.jumlah)

    def tampilPegawai(self):
        print("\nNama : ", self.nama)
        print("Gaji bulanan : ", self.gaji_bulanan, ", bonus: ", self.bonus)

    #Method Overloading
    def tunjangan(self, istri=None, anak=None):
        if anak != None and istri != None:
            total = anak + istri
            print("Tunjangan anak + istri = ", total)
        else:
            total = istri
            print("Tunjangan istri = ", total)

# Memanggil Kelas
namaPegawai = []
gajiBulanan = []
bonusPegawai = []

jml_peg = int(input("Masukan Jumlah Pegawai yang akan di input: "))
for i in range (1,jml_peg+1):
    nama = input(f"\nMasukan Nama Pegawai {i}: ")
    namaPegawai.append(nama)
    gaj = int(input(f"Masukan Gaji Pegawai {i}: "))
    gajiBulanan.append(gaj)
    bns = int(input(f"Masukan Bonus Pegawai {i}: "))
    bonusPegawai.append(bns)

print('\n')
print('='*50)
for i in range (jml_peg):
    for pe in range (1):
        pe = Pegawai(namaPegawai[i],gajiBulanan[i],bonusPegawai[i])
        pe.tampilPegawai()
        pe.tunjangan(2000,500)
        print(pe.hasil_tahunan())

print("\nTotal pegawai %d" % Pegawai.jumlah)
rataGaji=sum(gajiBulanan)/Pegawai.jumlah
print("\nRata-rata gaji = "+str(rataGaji))
print('\n')
print('='*50)
#peg1 = Pegawai('Eren', 2000, 500)
#peg2 = Pegawai('Luffy', 6000, 500)
#peg1.tampilPegawai()
#peg2.tampilPegawai()
#peg1.tunjangan(2500, 2000)  #Overloading
#peg2.tunjangan(2500)        #Overloading

#print("Total pegawai %d" % Pegawai.jumlah)
#rataGaji=(peg1.gaji_bulanan + peg2.gaji_bulanan)/Pegawai.jumlah
#print("Rata-rata gaji = "+str(rataGaji))

#print(peg1.hasil_tahunan())
#print(peg2.hasil_tahunan())
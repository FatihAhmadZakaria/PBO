class ComputerPart:
    def __init__(self,pabrikan,nama,jenis,harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, jumlah_core, harga, speed):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.jumlah_core = jumlah_core
        self.speed = speed

    def tampil(self):
        print("Processor ",self.pabrikan,self.nama," speed ",self.speed)
        print("Jumlah Core ",self.jumlah_core," Harga ",self.harga)

class RandomAcsessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, kapasitas, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas

    def tampil(self):
        print("RAM ",self.pabrikan,self.nama)
        print("Dengan kapasitas ",self.kapasitas,"Harga ",self.harga)

class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, kapasitas, rpm, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas
        self.rpm = rpm

    def tampil(self):
        print("Penyimpanan ",self.nama,self.pabrikan," RPM ",self.rpm)
        print("Kapasitas ",self.kapasitas," Harga ",self.harga)

p = Processor('Intel','Core I7 7740X',4350000,4,'4.3GHz')
m = RandomAcsessMemory('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
hdd = HardDiskSATA('Seagate','HDD 2.5 inch',295000,'500GB',7200)

parts = [p, m, hdd]
print("\t\t Overriding ")
print("="*45)
print("\t\tCOMPUTER PART")
print("="*45)
for part in parts :
    part.tampil()
print("="*45)
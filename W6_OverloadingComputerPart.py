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
    def __init__(self, pabrikan, nama, kapasitas):
        self.pabrikan = pabrikan
        self.nama = nama
        self.kapasitas = kapasitas

    def tampil(self,harga):
        print("RAM ",self.pabrikan,self.nama)
        print("Dengan kapasitas ",self.kapasitas,"Harga ",harga)

class HardDiskSATA(ComputerPart):
    def __init__(self, nama, rpm, harga):
        self.nama = nama
        self.harga = harga
        self.rpm = rpm

    def tampil(self,pabrikan,kapasitas):
        print("Penyimpanan ",self.nama,pabrikan," RPM ",self.rpm)
        print("Kapasitas ",kapasitas," Harga ",self.harga)

p = Processor('Intel','Core I7 7740X',4350000,4,'4.3GHz')
m = RandomAcsessMemory('V-Gen','DDR4 SODimm PC19200/2400MHz','4GB')
hdd = HardDiskSATA('HDD 2.5 inch',295000,7200)

parts = [p, m, hdd]
print("\t\t Overloading ")
print("="*45)
print("\t\tCOMPUTER PART")
print("="*45)
p.tampil()
m.tampil(328000)
hdd.tampil("Seagate","500GB")
print("="*45)
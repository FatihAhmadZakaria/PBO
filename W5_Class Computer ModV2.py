#Hierarchial Class
#5210411210_FATIH AHMAD ZAKARIA
class ComputerPart:
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
    def tampilkan(self) :
        print(f"Processor {self.pabrikan} {self.nama}")
        print(f"Harga : {self.harga}")

class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas
    def tampilkan(self) :
        print(f"RAM {self.pabrikan} {self.kapasitas} {self.nama}")
        print(f"Harga : {self.harga}")

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas
        self.rpm = rpm
    def tampilkan(self) :
        print(f"HDD {self.pabrikan} {self.kapasitas} {self.nama} {self.rpm}")
        print(f"Harga : {self.harga}")

p = Processor('Intel', "Core I5 12400", 2750000)
m = RandomAccessMemory('G.Skill TridentZ', 'DDR4 3200MHz',3950000, "16GB Dual Kit")
hdd = HardDiskSATA('Seagate', 'Ukuran 3.5 Inch', 840000, '2TB', '7200 RPM')
parts = [p, m, hdd]
print("="*45)
print("\t\tCOMPUTER PART")
print("="*45)
for part in parts :
    part.tampilkan()
print("="*45)
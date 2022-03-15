#Multilevel Class
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
        print(f"{self.pabrikan} {self.nama} Harga {self.harga}")

class RandomAccessMemory(Processor) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def tampilkan(self) :
        print(f"{self.pabrikan} {self.nama} Harga {self.harga}")

class HardDiskSATA(RandomAccessMemory) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def tampilkan(self) :
        print(f"{self.nama} {self.pabrikan} {self.harga}")

p = Processor('Intel', "Core I3 12100F", 1690000)
r = RandomAccessMemory('G.Skill TridentZ', 'DDR4 3200MHz',3950000)
hdd = HardDiskSATA('Seagate', 'HDD 3.5 inch', 840000)

parts = [p, r, hdd]
print("="*45)
print("\t\tCOMPUTER PART")
print("="*45)
for part in parts :
    part.tampilkan()
print("="*45)
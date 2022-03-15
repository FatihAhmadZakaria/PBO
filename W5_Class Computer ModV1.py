#Multiple Class
#5210411210_FATIH AHMAD ZAKARIA

class ComputerPart1():
    def __init__(self, pabrikan, nama) :
        self.pabrikan = pabrikan
        self.nama = nama

class ComputerPart2() :
    def __init__(self, harga) :
        self.harga = harga

class Processor(ComputerPart1, ComputerPart2) :
    def __init__(self, pabrikan, nama, harga) :
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def tampilkan(self) :
        print(f"{self.pabrikan} {self.nama}")
        print(f"Harga : {self.harga}")

class RandomAccessMemory(ComputerPart1, ComputerPart2) :
    def __init__(self, pabrikan, nama, harga) :
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def tampilkan(self) :
        print(f"{self.pabrikan} {self.nama}")
        print(f"Harga : {self.harga}")

class HardDiskSATA(ComputerPart1, ComputerPart2) :
    def __init__(self, pabrikan, nama, harga) :
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def tampilkan(self) :
        print(f"{self.pabrikan} {self.nama}")
        print(f"Harga : {self.harga}")

p = Processor('Intel', "Core I9 12600KF", 4040000)
m = RandomAccessMemory('G.Skill TridentZ', 'DDR4 3200MHz',3950000)
hdd = HardDiskSATA('Seagate', 'HDD 3.5 inch', 840000)

parts = [p, m, hdd]
print("="*45)
print("\t\tCOMPUTER PART")
print("="*45)
for part in parts :
    part.tampilkan()
print("="*45)
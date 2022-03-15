class ComputerPart:
    def __init__(self,pabrikan,nama,jenis,harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, jumlah_core, harga, speed):
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed = speed

class RandomAcsessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, kapasitas, harga):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas = kapasitas

class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, kapasitas, rpm, harga):
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm

p = Processor('Intel','Core I7 7740X',4350000,4,'4.3GHz')
m = RandomAcsessMemory('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
hdd = HardDiskSATA('Seagate','HDD 2.5 inch',295000,'500GB',7200)

parts = [p,m,hdd]
for part in parts:
    print('{} {} produksi {}'.format(part.jenis,part.nama,part.pabrikan))
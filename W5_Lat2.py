# Multilevel Inheritance

# Parent Class
class Hewan:
    def bersuara(self):
        print('Kucing bersuara')

# Child class mewarisi class Hewan
class Kucing(Hewan):
    def suara(self):
        print('meong...meong...meong...')

# Child class AnakKucing mewarisi dari class Hewan
class AnakKucing(Kucing):
    def minum(self):
        print('minum susu')

# Objek
ak=AnakKucing()
ak.bersuara()
ak.suara()
ak.minum()
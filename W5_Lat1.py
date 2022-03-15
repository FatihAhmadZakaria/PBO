# Single Inheritance

# Child Class
class Hewan:
    def bersuara(self):
        print('Kucing bersuara')

#Child class mewarisi class Hewan
class Kucing(Hewan):
    def suara(self):
        print('meong...meong...meong...')

#Objek
k=Kucing()
k.suara()
k.bersuara()
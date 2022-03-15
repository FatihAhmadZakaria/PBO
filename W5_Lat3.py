# Hierarchical Inheritance

#Class parent
class Induk:
    def fungsiInduk(self):
        print('Fungsi pada parent class.')

#Class turunan 1
class Anak1(Induk):
    def fungsianak1(self):
        print('Fungsi pada anak 1.')

#Class turunan 2
class Anak2(Induk):
    def fungsianak2(self):
        print('Fungsi pada akan 2.')

a1=Anak1()
a2=Anak2()

a1.fungsiInduk()
a1.fungsianak1()

a2.fungsiInduk()
a2.fungsianak2()
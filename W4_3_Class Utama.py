class Utama:
    def __init__(self):
        self._a = 2

class Turunan(Utama):
    def __init__(self):
        #Memanggil konstruktor pada kelas Utama
        Utama.__init__(self)
        print("Memanggil variabel protected pada class Utama: ",self._a)

        #Modify the protected variable:
        self._a = 3
        print("Memanggil variabel protected yang dimodifikasi diluar class: ",self._a)

objek1 = Turunan()
objek2 = Utama()

#Memanggil variabel protected
print("Mengakses variabel protected dari objek1: ", objek1._a)
print("Mengakses variabel protected dari objek1: ", objek2._a)
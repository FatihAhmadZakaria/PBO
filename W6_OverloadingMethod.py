#Overloading Method

class Aritmatika:
    def tambah(self, *daftarnilai):
        total=0
        for i in daftarnilai:
            total +=i
        return total

obj=Aritmatika()
print(obj.tambah(1, 2))
print(obj.tambah(20, 5, 10))
print(obj.tambah(4, 3, 2, 1))
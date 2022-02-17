#String
str='Aku cinta Indonesia'
print(str)

str=str[:10]+'tanah air ku'+str[9:]
print(str)

str=''
print(str)

str1='aku cinta tanah air ku Indonesia'
str1=str1[:9]+''+str1[22:]
print(str1)

kelas = 'praktikum pemrograman berorientasi objek'
up = kelas.upper()
lo = kelas.lower()
cap = kelas.capitalize()
print(kelas)
print(cap)
print(up)
print(lo)

s = '   Python  '
strip = s.strip()
ls = s.lstrip()
rs = s.rstrip()
print(s)
print(strip)
print(ls)
print(rs)

print("\nLen")
print (len(kelas))

jumlah = len(kelas)
print("Panjang string kelas adalah : ",jumlah)

print('')
s1 = 'Python'
s2 = 'Programing'
print(s1+s2)

print("\nIndeks")
print(kelas.index('a'))

print("\nIni replace")
kelas2 = kelas.replace('praktikum', 'praktik')
print(kelas2)

a = 'satu'
b = 'dua'
c = 'tiga'
print('\nsaya mempunyai %s mangga'%(b))

print('\nIni split')
print (kelas2.split())

print("\nIni input")
hari = input("Masukan Hari : ")
print("Hari ini adalah : ", hari)

data1 = int(input('\nAngka 1 : '))
data2 = int(input('Angka 2 : '))
hasil = int(data1*data2)
print(data1,'*',data2,' = ',hasil)

#LIST
print("\nIni LIST")
list = [0,1,2,3,4,5,6,7,8,9]
print(list)
print("List indeks 5 = ",list[5])
print(list[:3])
print(list[10-3:])
print(list[2:9])
print(list[-10])
print(list[0])

list.append(10)
print('Append')
print(list)

list.insert(1, 11)
print('Insert')
print(list)

list2 = ['halo']
list.extend(list2)
print("extend")
print(list)
list.extend('hai')
print(list)

del list[1]
print("del")
print(list)

list.remove(10)
print("remove")
print(list)

print("POP")
print(list.pop())
print(list)
#jika tidak di isi indeks adan otomatis mengambil indeks paling belakang

list.pop(2)
print(list)

a = [50,10,20,30,40]
b = sorted(a)
print("sortir")
print(b)
a.sort()
print(a)

a.sort(reverse=True)
print("reverse")
print(a)
#nilai reverse harus true atau false

min=min(a)
print(min)
max=max(a)
print(max)

#DICT
print('\nIni DICT')
d = {1:100, 2:200, 3:300, 4:400, 5:500}
print(d)

print(d[2])
print(d.get(4))
#get menggunakan key bukan indeks

print(d.keys())
print(d.values())
del d[1]
#del keys
print(d)

b = d.copy()
print(b)
d.clear()
print(d)
print(len(d))

#tuple
print('\nIni tuple')
t = (100,200,300,400)
print(t[0])
print(t[3])
t.index(200)

t2 = (10,20,10,30,10,40,20)
t2.count(10)
t2.count(30)
t2.count(20)

#SET (Himpunan)
print('\nIni SET')
setku = {'mencoba','set','atau','himpunan'}
print(setku)
#variabel yang sama hanya akan ditampilkan sekali
#urutan menampilkanya random / acak

#menambah elemen set
setku.add('elemen')
print(setku)
setku.update('kata') #update penambahanya per huruf
print(setku)

#menghapus elemen set
setku.discard('elemen')
print(setku)
setku.clear()
print(setku) #hanya tampil set kosong "set()"

#menyalin set
setku1 = {1,2,3,5,6,8,9}
setku2 = setku1.copy()
print('set 1 ',setku1)
setku2.add(10) #tambah elemen pada set 2 agar terlihat perbedaannya dengan set 1
print('set 2 ',setku2)

#mencari irisan
setku3 = {0,2,4,6,8,9}
print('set 3 ',setku3)
print('Intersection dari set 1 dan set 3 ',setku1.intersection(setku3))

#mencari selisih
print('set 1 defference set 3',setku1.difference(setku3))
print('set 3 defference set 1',setku3.difference(setku1))

#menggabungkan dua set
gabung = setku1.union(setku3)
print('set gabungan dari set 1 & 3', gabung)

#membuat elemen tidak dapat diubah
froze = frozenset(gabung)
print(froze)
import cx_Oracle

mydb = cx_Oracle.connect(
    "python",
    "python",
    "127.0.0.1/XE")

cur =mydb.cursor()

print("Connection is OK!")

while True:
    print("Menu\n1. Create DB\n2. Insert\n3. Edit\n4. Delete\n5. Select\n")
    mp1 = input("Masukan Pilihan\n")
    if mp1 == '1':
        print("Buat Tabel\n1. Dosen\n2. Kuliah\n3. Matakuliah\n")
        mt1 = input("Masukan Pilihan\n")
        if mt1 == '1':
            cur.execute('''CREATE TABLE dosen (
                            kode_dos VARCHAR(5) NOT NULL PRIMARY KEY,
                            nama_dos VARCHAR(225),
                            alamat_dos VARCHAR(225),
                            no_telp VARCHAR(15))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '2':
            cur.execute('''CREATE TABLE kuliah (
                            kode_mk VARCHAR(5) NOT NULL PRIMARY KEY,
                            kode_dos VARCHAR(5),
                            waktu VARCHAR(25),
                            tempat VARCHAR(225))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '3':
            cur.execute('''CREATE TABLE matakuliah (
                            kode_mk VARCHAR(5) NOT NULL PRIMARY KEY,
                            nama_mk VARCHAR(225),
                            sks DECIMAL(5),
                            semester VARCHAR(225))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        else:
            print("Input menu salah!!")
    elif mp1 == '2':
        print("Insert Data\n1. Dosen\n2. Kuliah\n3. MataKuliah\n")
        mt2 = input("Masukan Pilihan\n")
        if mt2 == '1':
            cur.execute('''INSERT INTO dosen VALUES ('D11', 'Harpuji','Jl.Kaliurang Km 13','088844556')''')
            cur.execute('''INSERT INTO dosen VALUES ('D12', 'Nana','Kota Gede','085422358')''')
            cur.execute('''INSERT INTO dosen VALUES ('D13', 'Ali Bedi','Magelang Kota','08994545244')''')
            cur.execute('''INSERT INTO dosen VALUES ('D14', 'Ninis','Gejayan','0815154795')''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '2':
            cur.execute('''INSERT INTO kuliah VALUES ('MK1','D11','Senin 07.00-8.40','K.0.1')''')
            cur.execute('''INSERT INTO kuliah VALUES ('MK2','D12','Selasa 09.40-11.20','D.2.1')''')
            cur.execute('''INSERT INTO kuliah VALUES ('MK3','D13','Rabu 08.50-10.20','E.3.1')''')
            cur.execute('''INSERT INTO kuliah VALUES ('MK4','D14','Kamis 14.40-16.20','B.0.3')''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '3':
            cur.execute('''INSERT INTO matakuliah VALUES ('MK1','Aplikasi Kantor',2,'Semester 2')''')
            cur.execute('''INSERT INTO matakuliah VALUES ('MK2','Rekayasa Web',3,'Semester 2')''')
            cur.execute('''INSERT INTO matakuliah VALUES ('MK3','Web Mobile',3,'Semester 1')''')
            cur.execute('''INSERT INTO matakuliah VALUES ('MK4','English',2,'Semester 2')''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        else:
            print("Input menu salah!!")
    elif mp1 == '3':
        print("Update Data\n1. Dosen\n2. Kuliah\n3. MataKuliah\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'dosen'
            v = '''nama_dos = 'Dani' WHERE kode_dos = 'D11'
            '''
            o = 'Update Dosen'
        elif  mt3 == '2':
            p = 'kuliah'
            v = '''Tempat = 'K.3.3' WHERE kode_mk = 'MK4'
            '''
            o = 'Update Kuliah'
        elif mt3 == '3':
            p = 'matakuliah'
            v = '''semester = 'Semester 1' WHERE kode_mk = 'MK2'
            '''
            o = 'Update MataKuliah'
        else:
            print("Salah Input!!")
        cur.execute(f"UPDATE {p} SET {v}")
        mydb.commit()
        print(o)
    elif mp1 == '4':
        print("Delete Data\n1. Dosen\n2. Kuliah\n3. MataKuliah\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'dosen'
            v = '''kode_dos = 'D14'
            '''
            o = 'Delete Dosen'
        elif  mt3 == '2':
            p = 'kuliah'
            v = '''kode_mk = 'MK3'
            '''
            o = 'Delete kuliah'
        elif mt3 == '3':
            p = 'matakuliah'
            v = '''kode_mk = 'MK1'
            '''
            o = 'Delete matakuliah'
        else:
            print("Salah Input!!")
        cur.execute(f"DELETE FROM {p} WHERE {v}")
        mydb.commit()
        print(o)
    elif mp1 == '5':
        print("Select Tabel\n1. Dosen\n2. Kuliah\n3. MataKuliah\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'dosen'
        elif  mt3 == '2':
            p = 'kuliah'
        elif mt3 == '3':
            p = 'matakuliah'
        else:
            print("Salah Input!!")
        cur.execute(f"SELECT * FROM {p}")
        res = cur.fetchall()
        for row in res:
            print (row,'\n')
    elif mp1 == '0':
        cur.close()
        mydb.close()
        print("Selesai")
        break
    else:
        print("Salah Input!")
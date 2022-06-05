import cx_Oracle

mydb = cx_Oracle.connect(
    "python",
    "python",
    "127.0.0.1/XE")

cur =mydb.cursor()

print("Connection is OK!")
while True:
    print("1. Buat Tabel\n2. Insert\n3. Update\n4. Delete\n5. Select\n0. Keluar")
    mp1 = input("Masukan Pilihan\n")
    if mp1 == '1':
        print("Buat Tabel\n1. Jabatan\n2. Pegawai\n3. Gaji\n4. Golongan\n")
        mt1 = input("Masukan Pilihan\n")
        if mt1 == '1':
            cur.execute('''CREATE TABLE jabatan (
                            kode_jabatan VARCHAR(3) NOT NULL PRIMARY KEY,
                            nama_jabatan VARCHAR(40),
                            gapok DECIMAL(10),
                            tunjangan_jabatan DECIMAL(10))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '2':
            cur.execute('''CREATE TABLE pegawai (
                            nip VARCHAR(20) NOT NULL PRIMARY KEY,
                            nama_pegawai VARCHAR(40),
                            kode_jabatan VARCHAR(3),
                            kode_golongan VARCHAR(3),
                            status VARCHAR(15),
                            jumlah_anak DECIMAL(2))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '3':
            cur.execute('''CREATE TABLE gaji (
                            bulanan VARCHAR(20) NOT NULL PRIMARY KEY,
                            nip VARCHAR(20),
                            masuk DECIMAL(5),
                            sakit DECIMAL(5),
                            ijin DECIMAL(5),
                            alpha DECIMAL(5),
                            lembur DECIMAL(5),
                            potongan DECIMAL(10))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '4':
            cur.execute('''CREATE TABLE golongan (
                            kode_golongan VARCHAR(3) NOT NULL PRIMARY KEY,
                            nama_golongan VARCHAR(15),
                            tunjangan_suami DECIMAL(10),
                            tunjangan_anak DECIMAL(10),
                            uang_makan DECIMAL(10),
                            uang_lembur DECIMAL(10),
                            akses DECIMAL(10))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        else:
            print("Input menu salah!!")
    elif mp1 == '2':
        print("Insert Data\n1. Jabatan\n2. Pegawai\n3. Gaji\n4. Golongan\n")
        mt2 = input("Masukan Pilihan\n")
        if mt2 == '1':
            cur.execute('''INSERT INTO jabatan VALUES ('M01','Manajer',100000,5000)''')
            cur.execute('''INSERT INTO jabatan VALUES ('A01','Assisten',50000,3000)''')
            cur.execute('''INSERT INTO jabatan VALUES ('B01','Bendahara',40000,2000)''')
            cur.execute('''INSERT INTO jabatan VALUES ('S01','Sekertaris',40000,2000)''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '2':
            cur.execute('''INSERT INTO pegawai VALUES ('3321001','Carl Johnson','M01','G01','Berkeluarga',3)''')
            cur.execute('''INSERT INTO pegawai VALUES ('3321002','Trevor','A01','G01','Berkeluarga',1)''')
            cur.execute('''INSERT INTO pegawai VALUES ('3321003','Michel','B01','G01','Berkeluarga',2)''')
            cur.execute('''INSERT INTO pegawai VALUES ('3321004','Franklin','S01','G02','Single',0)''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '3':
            cur.execute('''INSERT INTO gaji VALUES ('1000000','M01',30,0,0,0,15,0)''')
            cur.execute('''INSERT INTO gaji VALUES ('900000','A01',10,0,5,15,0,500000)''')
            cur.execute('''INSERT INTO gaji VALUES ('800000','B01',25,3,1,1,10,0)''')
            cur.execute('''INSERT INTO gaji VALUES ('700000','S01',30,0,0,0,10,0)''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '4':
            cur.execute('''INSERT INTO golongan VALUES ('G01','Keluarga',200000,100000,100000,20000,50000)''')
            cur.execute('''INSERT INTO golongan VALUES ('G02','Single',0,0,150000,20000,50000)''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        else:
            print("Input menu salah!!")
    elif mp1 == '3':
        print("Update Data\n1. Jabatan\n2. Pegawai\n3. Gaji\n4. Golongan\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'jabatan'
            v = '''gapok = 150000 WHERE kode_jabatan = 'M01'
            '''
            o = 'Update Jabatan'
        elif  mt3 == '2':
            p = 'pegawai'
            v = '''jumlah_anak = 2 WHERE nip = '3321001'
            '''
            o = 'Update Pegawai'
        elif mt3 == '3':
            p = 'gaji'
            v = '''potongan = 150000 WHERE nip = 'A01'
            '''
            o = 'Update gaji'
        elif mt3 == '4':
            p = 'golongan'
            v = '''uang_makan = 125000 WHERE kode_golongan = 'G02'
            '''
            o = 'Update Golongan'
        else:
            print("Salah Input!!")
        cur.execute(f"UPDATE {p} SET {v}")
        mydb.commit()
        print(o)
    elif mp1 == '4':
        print("Delete Data\n1. Jabatan\n2. Pegawai\n3. Gaji\n4. Golongan\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'jabatan'
            v = '''kode_jabatan = 'A01'
            '''
            o = 'Delete Jabatan'
        elif  mt3 == '2':
            p = 'pegawai'
            v = '''nip = '3321002'
            '''
            o = 'Delete Update Pegawai'
        elif mt3 == '3':
            p = 'gaji'
            v = '''nip = 'A01'
            '''
            o = 'Delete Update gaji'
        elif mt3 == '4':
            p = 'golongan'
            v = '''kode_golongan = 'G02'
            '''
            o = 'Delete Update Golongan'
        else:
            print("Salah Input!!")
        cur.execute(f"DELETE FROM {p} WHERE {v}")
        mydb.commit()
        print(o)
    elif mp1 == '5':
        print("Select Tabel\n1. Jabatan\n2. Pegawai\n3. Gaji\n4. Golongan\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'jabatan'
        elif  mt3 == '2':
            p = 'pegawai'
        elif mt3 == '3':
            p = 'gaji'
        elif mt3 == '4':
            p = 'golongan'
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
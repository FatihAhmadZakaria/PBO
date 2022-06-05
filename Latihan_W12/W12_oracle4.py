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
        print("Buat Tabel\n1. Nasabah\n2. Transaksi\n3. Rekening\n4. Cabang Bank\n")
        mt1 = input("Masukan Pilihan\n")
        if mt1 == '1':
            cur.execute('''CREATE TABLE nasabah (
                            id_nasabah VARCHAR(5) NOT NULL PRIMARY KEY,
                            nama_nas VARCHAR(225),
                            alamat_nas VARCHAR(225))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '2':
            cur.execute('''CREATE TABLE transaksi_bank (
                            no_tran VARCHAR(5) NOT NULL PRIMARY KEY,
                            jenis_nas VARCHAR(225),
                            tanggal VARCHAR(25),
                            jumlah  DECIMAL(25))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '3':
            cur.execute('''CREATE TABLE rekening (
                            no_rek VARCHAR(11) NOT NULL PRIMARY KEY,
                            pin VARCHAR(25),
                            saldo DECIMAL(25))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '4':
            cur.execute('''CREATE TABLE cabang_bank (
                            kode_cab VARCHAR(5) NOT NULL PRIMARY KEY,
                            nama_cab VARCHAR(25),
                            alamat_cab VARCHAR(225))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        else:
            print("Input menu salah!!")
    elif mp1 == '2':
        print("Insert Data\n1. Nasabah\n2. Transaksi\n3. Rekening\n4. Cabang Bank\n")
        mt2 = input("Masukan Pilihan\n")
        if mt2 == '1':
            cur.execute('''INSERT INTO nasabah VALUES ('N011','Dinda','Jl.Gedongan')''')
            cur.execute('''INSERT INTO nasabah VALUES ('N012','Danesya','Jl.Sorowajan')''')
            cur.execute('''INSERT INTO nasabah VALUES ('N013','Maharini','Jl.Sorogedug')''')
            cur.execute('''INSERT INTO nasabah VALUES ('N014','Aisyah','Jl.Nanggulan')''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '2':
            cur.execute('''INSERT INTO transaksi_bank VALUES ('T011','Debitur','09-03-2022',2000000)''')
            cur.execute('''INSERT INTO transaksi_bank VALUES ('T012','Penyimpanan','10-03-2022',1500000)''')
            cur.execute('''INSERT INTO transaksi_bank VALUES ('T013','Debitur','15-03-2022',100000)''')
            cur.execute('''INSERT INTO transaksi_bank VALUES ('T014','Penyimpanan','19-03-2022',300000)''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '3':
            cur.execute('''INSERT INTO rekening VALUES ('075458869','454545','3000000')''')
            cur.execute('''INSERT INTO rekening VALUES ('485754855','658595','4000000')''')
            cur.execute('''INSERT INTO rekening VALUES ('998582235','754819','1000000')''')
            cur.execute('''INSERT INTO rekening VALUES ('125488556','162358','1500000')''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '4':
            cur.execute('''INSERT INTO cabang_bank VALUES ('CB1','Cab.Ngaglik','Jl.Kaliurang Km 14')''')
            cur.execute('''INSERT INTO cabang_bank VALUES ('CB2','Cab.Pendowo','Jl.Ringin Sawit 2')''')
            cur.execute('''INSERT INTO cabang_bank VALUES ('CB3','Cab.Kraton','Jl.DalemKraton')''')
            cur.execute('''INSERT INTO cabang_bank VALUES ('CB4','Cab.Kotagede','Jl.Gedeagung')''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        else:
            print("Input menu salah!!")
    elif mp1 == '3':
        print("Update Data\n1. Nasabah\n2. Transaksi\n3. Rekening\n4. Cabang Bank\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'nasabah'
            v = '''nama_nas = 'Sheila' WHERE id_nasabah = 'N011'
            '''
            o = 'Update Nasabah'
        elif  mt3 == '2':
            p = 'transaksi_bank'
            v = '''jenis_nas = 'Debitur' WHERE no_tran = 'T012'
            '''
            o = 'Update transaksi'
        elif mt3 == '3':
            p = 'rekening'
            v = '''pin = '852525' WHERE no_rek = '075458869'
            '''
            o = 'Update rekening'
        elif mt3 == '4':
            p = 'cabang_bank'
            v = '''nama_cab = 'Cab.Kalasan' WHERE kode_cab = 'CB3'
            '''
            o = 'Update Cabang Bank'
        else:
            print("Salah Input!!")
        cur.execute(f"UPDATE {p} SET {v}")
        mydb.commit()
        print(o)
    elif mp1 == '4':
        print("Delete Data\n1. Nasabah\n2. Transaksi\n3. Rekening\n4. Cabang Bank\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'nasabah'
            v = '''id_nasabah = 'N014'
            '''
            o = 'Delete Nasabah'
        elif  mt3 == '2':
            p = 'transaksi_bank'
            v = '''no_tran = 'T013'
            '''
            o = 'Delete Transaksi'
        elif mt3 == '3':
            p = 'rekening'
            v = '''no_rek = '125488556'
            '''
            o = 'Delete Nota'
        elif mt3 == '4':
            p = 'cabang_bank'
            v = '''kode_cab = 'CB4'
            '''
            o = 'Delete Cabang Bank'
        else:
            print("Salah Input!!")
        cur.execute(f"DELETE FROM {p} WHERE {v}")
        mydb.commit()
        print(o)
    elif mp1 == '5':
        print("Select Tabel\n1. Nasabah\n2. Transaksi\n3. Rekening\n4. Cabang Bank\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'nasabah'
        elif  mt3 == '2':
            p = 'transaksi_bank'
        elif mt3 == '3':
            p = 'rekening'
        elif mt3 == '4':
            p = 'cabang_bank'
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
import sqlite3

mydb = sqlite3.connect("Latihan_1")
cur = mydb.cursor()

print("Connection is OK!")

while True:
    print("Menu\n1. Create DB\n2. Insert\n3. Edit\n4. Delete")
    mp1 = input("Masukan Pilihan\n")
    if mp1 == '1':
        print("Buat Tabel\n1. Nasabah\n2. Barang\n3. Nota\n4. Transaksi\n")
        mt1 = input("Masukan Pilihan\n")
        if mt1 == '1':
            cur.execute('''CREATE TABLE nasabah (
                            id_nasabah VARCHAR(5) NOT NULL PRIMARY KEY,
                            nama_nas VARCHAR(225),
                            alamat_nas TEXT)''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '2':
            cur.execute('''CREATE TABLE transaksi_bank (
                            no_tran VARCHAR(5) NOT NULL PRIMARY KEY,
                            jenis_nas VARCHAR(225),
                            tanggal VARCHAR(25),
                            jumlah  INTEGER(25))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '3':
            cur.execute('''CREATE TABLE rekening (
                            no_rek VARCHAR(11) NOT NULL PRIMARY KEY,
                            pin VARCHAR(25),
                            saldo INTEGER(25))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '4':
            cur.execute('''CREATE TABLE cabang_bank (
                            kode_cab VARCHAR(5) NOT NULL PRIMARY KEY,
                            nama_cab VARCHAR(25),
                            alamat_cab TEXT)''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        else:
            print("Input menu salah!!")
    elif mp1 == '2':
        print("Insert Data\n1. nasabah\n2. transaksi\n3. rekening\n4. cabang_bank\n")
        mt2 = input("Masukan Pilihan\n")
        if mt2 == '1':
            cur.execute('''INSERT INTO nasabah VALUES
                            ("N011","Dinda","Jl.Gedongan"),
                            ("N012","Danesya","Jl.Sorowajan"),
                            ("N013","Maharini","Jl.Sorogedug"),
                            ("N014","Aisyah","Jl.Nanggulan")''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '2':
            cur.execute('''INSERT INTO transaksi_bank VALUES
                            ("T011","Debitur","09-03-2022",2000000),
                            ("T012","Penyimpanan","10-03-2022",1500000),
                            ("T013","Debitur","15-03-2022",100000),
                            ("T014","Penyimpanan","19-03-2022",300000)''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '3':
            cur.execute('''INSERT INTO rekening VALUES
                            ("075458869","454545","3000000"),
                            ("485754855","658595","4000000"),
                            ("998582235","754819","1000000"),
                            ("125488556","162358","1500000")''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '4':
            cur.execute('''INSERT INTO cabang_bank VALUES
                            ("CB1","Cab.Ngaglik","Jl.Kaliurang Km 14"),
                            ("CB2","Cab.Pendowo","Jl.Ringin Sawit 2"),
                            ("CB3","Cab.Kraton","Jl.DalemKraton"),
                            ("CB4","Cab.Kotagede","Jl.Gedeagung")''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        else:
            print("Input menu salah!!")
    elif mp1 == '3':
        print("Update Data\n1. nasabah\n2. transaksi\n3. rekening\n4. cabang_bank\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'nasabah'
            v = 'nama_nas = "Sheila" WHERE id_nasabah = "N011"'
            o = 'Update Nasabah'
        elif  mt3 == '2':
            p = 'transaksi_bank'
            v = 'jenis_nas = "Debitur" WHERE no_tran = "T012"'
            o = 'Update transaksi'
        elif mt3 == '3':
            p = 'rekening'
            v = 'pin = "852525" WHERE no_rek = "075458869"'
            o = 'Update rekening'
        elif mt3 == '4':
            p = 'cabang_bank'
            v = 'nama_cab = "Cab.Kalasan" WHERE kode_cab = "CB3"'
            o = 'Update Cabang Bank'
        else:
            print("Salah Input!!")
        cur.execute(f"UPDATE {p} SET {v}")
        mydb.commit()
        print(o)
    elif mp1 == '4':
        print("Delete Data\n1. nasabah\n2. transaksi\n3. rekening\n4. cabang_bank\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'nasabah'
            v = 'id_nasabah = "N014"'
            o = 'Delete Nasabah'
        elif  mt3 == '2':
            p = 'transaksi_bank'
            v = 'no_tran = "T013"'
            o = 'Delete Transaksi'
        elif mt3 == '3':
            p = 'rekening'
            v = 'no_rek = "125488556"'
            o = 'Delete Nota'
        elif mt3 == '4':
            p = 'cabang_bank'
            v = 'kode_cab = "CB4"'
            o = 'Delete Cabang Bank'
        else:
            print("Salah Input!!")
        cur.execute(f"DELETE FROM {p} WHERE {v}")
        mydb.commit()
        print(o)
    elif mp1 == '5':
        print("Select Tabel\n1. nasabah\n2. transaksi\n3. rekening\n4. cabang_bank\n")
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
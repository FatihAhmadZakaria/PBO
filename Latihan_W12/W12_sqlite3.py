import sqlite3

mydb = sqlite3.connect("Latihan_1")
cur = mydb.cursor()

print("Connection is OK!")

while True:
    print("Menu\n1. Create DB\n2. Insert\n3. Edit\n4. Delete")
    mp1 = input("Masukan Pilihan\n")
    if mp1 == '1':
        print("Buat Tabel\n1. Suppiler\n2. Barang\n3. Nota\n4. Transaksi\n")
        mt1 = input("Masukan Pilihan\n")
        if mt1 == '1':
            cur.execute('''CREATE TABLE supplier (
                            kode_sup VARCHAR(5) NOT NULL PRIMARY KEY,
                            nama_sup VARCHAR(225))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '2':
            cur.execute('''CREATE TABLE barang (
                            kode_bar VARCHAR(5) NOT NULL PRIMARY KEY,
                            nama_bar VARCHAR(225))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '3':
            cur.execute('''CREATE TABLE nota (
                            no_nota VARCHAR(5) NOT NULL PRIMARY KEY,
                            tanggal VARCHAR(25),
                            tempo VARCHAR(25),
                            total VARCHAR(225),
                            kode_sup VARCHAR(5))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        elif mt1 == '4':
            cur.execute('''CREATE TABLE transaksi (
                            no_nota VARCHAR(5) NOT NULL PRIMARY KEY,
                            kode_bar VARCHAR(25),
                            qty INTEGER(5),
                            harga VARCHAR(225))''')
            mydb.commit()
            print("Buat Tabel Selesai!")
        else:
            print("Input menu salah!!")
    elif mp1 == '2':
        print("Insert Data\n1. Supplier\n2. Barang\n3. Nota\n4. Transaksi\n")
        mt2 = input("Masukan Pilihan\n")
        if mt2 == '1':
            cur.execute('''INSERT INTO supplier VALUES
                            ("SP1","PT.Tembakau"),
                            ("SP2","PT.Roki"),
                            ("SP3","PT.Tenka"),
                            ("SP4","PT.LENT")''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '2':
            cur.execute('''INSERT INTO barang VALUES
                            ("B11","Gudang Garam"),
                            ("B12","Kopi ABC"),
                            ("B13","Nutrisari"),
                            ("B14","GoodDay")''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '3':
            cur.execute('''INSERT INTO nota VALUES
                            ("N001","07-11-2021","17-11-2021","Rp.900.000","SP1"),
                            ("N002","05-10-2021","15-10-2021","Rp.850.000","SP2"),
                            ("N003","09-11-2021","19-11-2021","Rp.700.000","SP3"),
                            ("N004","10-11-2021","20-11-2021","Rp.500.000","SP4")''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        elif mt2 == '4':
            cur.execute('''INSERT INTO transaksi VALUES
                            ("N001","B11",30,"Rp.30.000"),
                            ("N002","B12",25,"Rp.34.000"),
                            ("N003","B13",35,"Rp.20.000"),
                            ("N004","B14",50,"Rp.10.000")''')
            mydb.commit()
            print("Insert Tabel Selesai!")
        else:
            print("Input menu salah!!")
    elif mp1 == '3':
        print("Update Data\n1. Supplier\n2. Barang\n3. Nota\n4. Transaksi\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'supplier'
            v = 'nama_sup = "PT.Rokok" WHERE kode_sup = "SP1"'
            o = 'Update supplier'
        elif  mt3 == '2':
            p = 'barang'
            v = 'nama_bar = "Momogi" WHERE kode_bar = "B12"'
            o = 'Update barang'
        elif mt3 == '3':
            p = 'nota'
            v = 'tempo = "15-11-2021" WHERE no_nota = "N001"'
            o = 'Update Nota'
        elif mt3 == '4':
            p = 'transaksi'
            v = 'qty = 65 WHERE no_nota = "N004"'
            o = 'Update Transaksi'
        else:
            print("Salah Input!!")
        cur.execute(f"UPDATE {p} SET {v}")
        mydb.commit()
        print(o)
    elif mp1 == '4':
        print("Delete Data\n1. Supplier\n2. Barang\n3. Nota\n4. Transaksi\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'supplier'
            v = 'kode_sup = "SP2"'
            o = 'Delete Supplier'
        elif  mt3 == '2':
            p = 'barang'
            v = 'kode_bar = "B13"'
            o = 'Delete Barang'
        elif mt3 == '3':
            p = 'nota'
            v = 'no_nota = "N003"'
            o = 'Delete Nota'
        elif mt3 == '4':
            p = 'transaksi'
            v = 'no_nota = "N002"'
            o = 'Delete transaksi'
        else:
            print("Salah Input!!")
        cur.execute(f"DELETE FROM {p} WHERE {v}")
        mydb.commit()
        print(o)
    elif mp1 == '5':
        print("Select Tabel\n1. Supplier\n2. Barang\n3. Nota\n4. Transaksi\n")
        mt3 = input("Masukan Pilihan\n")
        if mt3 == '1':
            p = 'supplier'
        elif  mt3 == '2':
            p = 'barang'
        elif mt3 == '3':
            p = 'nota'
        elif mt3 == '4':
            p = 'transaksi'
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
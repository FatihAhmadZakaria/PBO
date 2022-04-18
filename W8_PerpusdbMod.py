import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perpus"
)
cur=mydb.cursor()

def tambah():
    while True:
        print("1. Buku\n2. Majalah\n3. DVD\n0. Kembali ke menu utama")
        pil = input("-->Masukan pilihan\n")
        if pil == '1':
            id_buku = input("-->Masukan ID baru\n")
            subjek = input("-->Jenis\n")
            judul = input("-->Masukan Judul\n")
            penulis = input("-->Masukan Penulis\n")
            info = input("-->Masukan Info\n")
            stok = int(input("-->Masukan Stok\n"))
            cur.execute("INSERT INTO data_buku(id_buku, subjek, judul, penulis, info, stok) VALUES (%s,%s,%s,%s,%s,%s)",(id_buku,subjek,judul,penulis,info,stok))
            mydb.commit()
            print("Data tersimpan...")
        elif pil == '2':
            id_buku = input("-->Masukan ID baru\n")
            judul = input("-->Masukan Judul\n")
            vol = input("-->Masukan Vol Majalah\n")
            issue = input("-->Masukan Issue\n")
            info = input("-->Masukan Info\n")
            stok = int(input("-->Masukan Stok\n"))
            cur.execute("INSERT INTO data_majalah(id_buku, judul, vol, issue, info, stok) VALUES (%s,%s,%s,%s,%s,%s)",(id_buku,judul,vol,issue,info,stok))
            mydb.commit()
            print("Data tersimpan...")
        elif pil == '3':
            id_buku = input("-->Masukan ID baru\n")
            judul = input("-->Masukan Judul\n")
            info = input("-->Masukan Info\n")
            stok = int(input("-->Masukan Stok\n"))
            cur.execute("INSERT INTO data_dvd(id_buku, judul, info, stok) VALUES (%s,%s,%s,%s)",(id_buku,judul,info,stok))
            mydb.commit()
            print("Data tersimpan...")
        elif pil == '0':
            input("Tekan enter untuk kembali...")
            break
        else:
            print("Masukan dengan benar!")

def tampilkan():
    cur.execute("select * from data_buku")
    db = cur.fetchall()
    print("\nBuku")
    for row in db:
        print(row)

    cur.execute("select * from data_majalah")
    print("\nMajalah")
    db = cur.fetchall()
    for row in db:
        print(row)

    cur.execute("select * from data_dvd")
    print("\nDVD")
    db = cur.fetchall()
    for row in db:
        print(row)

def update_stok():
    while True:
        print("1. Buku\n2. Majalah\n3. DVD\n0. Kembali ke menu utama")
        pil = input("-->Masukan pilihan\n")
        if pil == '1':
            id_buku = input("-->Masukan id buku\n ")
            jml_stok = input("-->Masukan Stok saat ini \n")
            cur.execute("UPDATE data_buku SET stok=%s WHERE id_buku=%s",(jml_stok,id_buku))
            mydb.commit()
            print("Update sukses...")
        elif pil == '2':
            id_buku = input("-->Masukan id buku\n ")
            jml_stok = input("-->Masukan Stok saat ini \n")
            cur.execute("UPDATE data_majalah SET stok=%s WHERE id_buku=%s",(jml_stok,id_buku))
            mydb.commit()
            print("Update sukses...")
        elif pil == '3':
            id_buku = input("-->Masukan id buku\n ")
            jml_stok = input("-->Masukan Stok saat ini \n")
            cur.execute("UPDATE data_dvd SET stok=%s WHERE id_buku=%s",(jml_stok,id_buku))
            mydb.commit()
            print("Update sukses...")
        elif pil == '0':
            input("Tekan enter untuk kembali...")
            break
        else:
            print("Masukan dengan benar!")

def hapus():
    while True:
        print("1. Buku\n2. Majalah\n3. DVD\n0. Kembali ke menu utama")
        pil = input("-->Masukan pilihan\n")
        if pil == '1':
            id_buku = input("-->Masukan id yang akan dihapus\n")
            cur.execute("DELETE FROM data_buku WHERE id_buku=%s",(id_buku,))
            mydb.commit()
            print("Hapus Sukses..")
        elif pil == '2':
            id_buku = input("-->Masukan id yang akan dihapus\n")
            cur.execute("DELETE FROM data_majalah WHERE id_buku=%s",(id_buku,))
            mydb.commit()
            print("Hapus Sukses..")
        elif pil == '3':
            id_buku = input("-->Masukan id yang akan dihapus\n")
            cur.execute("DELETE FROM data_dvd WHERE id_buku=%s",(id_buku,))
            mydb.commit()
            print("Hapus Sukses..")
        elif pil == '0':
            input("Tekan enter untuk kembali...")
            break
        else:
            print("Masukan dengan benar!")

def cari_buku():
    while True:
        print("\n1. Buku\n2. Majalah\n3. DVD\n0. Kembali ke menu utama")
        pil = input("-->Masukan pilihan\n")
        if pil == '1':
            id_buku = input("-->Masukan id yang dicari\n")
            cur.execute("SELECT * FROM data_buku WHERE id_buku=%s",(id_buku,))
            p = cur.fetchall()
            print(p)
        elif pil == '2':
            id_buku = input("-->Masukan id yang dicari\n")
            cur.execute("SELECT * FROM data_majalah WHERE id_buku=%s",(id_buku,))
            p = cur.fetchall()
            print(p)
        elif pil == '3':
            id_buku = input("-->Masukan id yang dicari\n")
            cur.execute("SELECT * FROM data_dvd WHERE id_buku=%s",(id_buku,))
            p = cur.fetchall()
            print(p)
        elif pil == '0':
            input("Tekan enter untuk kembali...")
            break
        else:
            print("Masukan dengan benar!")

def pinjam_kembali():
    while True:
        print("\n1. Pinjam\n2. Kembali\n0. Kembali ke menu utama")
        pil = input("-->Masukan pilihan\n")
        if pil == '1':
            id_buku = input("-->Masukan id\n")
            subjek = input("-->Jenis\n")
            nama = input("-->Masukan Nama peminjam\n")
            jumlah = input("-->Masukan jumlah\n")
            now = datetime.datetime.now()
            kembali = input("-->Masukan Tanggal Kembali (Ex : 2022-12-23)\n")
            cur.execute("INSERT INTO peminjam(subjek, id_buku, nama, tgl_keluar, jumlah, kembali) VALUES (%s,%s,%s,%s,%s,%s)",(subjek,id_buku,nama,now.strftime('%Y-%m-%d %H:%M:%S'),jumlah,kembali))
            mydb.commit()
            print("Data Pinjam di simpan..")
        elif pil == '2':
            id_buku = input("-->Masukan id\n")
            subjek = input("-->Jenis\n")
            nama = input("-->Masukan Nama peminjam\n")
            jumlah = input("-->Masukan jumlah\n")
            now = datetime.datetime.now()
            cur.execute("INSERT INTO kembali(subjek, id_buku, nama, tgl_kembali, jumlah) VALUES (%s,%s,%s,%s,%s)",(subjek,id_buku,nama,now.strftime('%Y-%m-%d %H:%M:%S'),jumlah))
            mydb.commit()
            print("Data Kembali di simpan..")
        elif pil == '0':
            input("Tekan enter untuk kembali...")
            break
        else:
            print("Masukan dengan benar!")

def rec_pinjam_kembali():
    while True:
        print("\nHistory\n1. Pinjam\n2. Pengembalian\n0. Kembali ke menu utama")
        pil = input("-->Masukan pilihan\n")
        if pil == '1':
            print("\nData Pinjam Buku\n")
            cur.execute("select * from peminjam")
            db = cur.fetchall()
            for row in db:
                print(row)
        elif pil == '2':
            print("\nData Pengembalian Buku\n")
            cur.execute("select * from kembali")
            db = cur.fetchall()
            for row in db:
                print(row)
        elif pil == '0':
            input("Tekan enter untuk kembali...")
            break
        else:
            print("Masukan dengan benar!")

print('='*10,"Selamat Data di Perpustakan UTY",'='*10)
while True:
        print("\nMenu Utama")
        print("1. Tambah Data")
        print("2. Tampilkan Semua")
        print("3. Update Stock")
        print("4. Hapus Data")
        print("5. Cari Buku")
        print("6. Pinjam / Kembali Buku")
        print("7. History Pinjam / Kembali")
        print("0. Keluar")
        pilihan = input("\n-->Masukan Pilihan : ")
        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            update_stok()
        elif pilihan == '4':
            hapus()
        elif pilihan == '5':
            cari_buku()
        elif pilihan == '6':
            pinjam_kembali()
        elif pilihan == '7':
            rec_pinjam_kembali()
        elif pilihan == '0':
            print("\nTerimakasih ^^\n")
            break
        else:
            print("Masukan dengan benar!")
import cx_Oracle

mydb = cx_Oracle.connect(
    "python",
    "python",
    "127.0.0.1/XE")

cur =mydb.cursor()

print("Connection is OK!")

cur.execute('''DROP TABLE cabang_bank ''')
mydb.commit()
print("Terhapus")
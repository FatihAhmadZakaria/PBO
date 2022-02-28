#titik dibentuk posisi pada sumbu x dan y
class Titik:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#garis dibentuk dari dua titik
class Garis:
    def __init__(self,titik_pertama,titik_kedua):
        self.titik_pertama = titik_pertama
        self.titik_kedua = titik_kedua
    
    def pajang(self):
        pjg_x = self.titik_kedua.x - self.titik_pertama.x
        pjg_y = self.titik_kedua.y - self.titik_pertama.y
        pjg = (pjg_x**2 + pjg_y**2) ** 0.5
        return pjg

titik_a = Titik(0,0)
titik_b = Titik(3,4)
garis_ab = Garis(titik_a,titik_b)
print('Panjang garis AB adalah {}'.format(garis_ab.pajang()))
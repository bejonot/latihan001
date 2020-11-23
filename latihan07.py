#Dictionary & Tuple
#Latihan supaya temen-temen pemanasan

#Latihan data struktur list
#List hanya butuh = []
#List hanya kumpulan deret data
#Isinya bisa number, bisa string, bisa list sendiri, bisa tuple, bisa dictionary sendiri
ListContoh = [5, 2, 3, "Luke", {"name": "John Doe"}]
ListSatu = [8,3,5,2]
print(ListContoh)
#Beberapa function untuk memanipulasi list
ListContoh.append("Padme")
print(ListContoh)
ListContoh.remove(5)
print(ListContoh)
del ListContoh[0]
print(ListContoh)

ListContoh[1:3]
#ListContoh.sort() # sifatnya permanen
ListSatu.sort()
print(ListSatu)
newlist = sorted(ListSatu)
print(ListSatu)
#newlist = sorted(ListContoh) #sifatnya temporary

#Dictionary = {}
Contoh_Dict = {"hero": "Batman", "color" : "Black"}
#Index hero = 0, isinya Batman
#Index color, isinya black
#Satu dictionary isinya bisa string ataupun nomor, bahkan bisa list
Contoh_Dict_2 = {"point": 15, "list": [2,3,4]}
#Set mirip dictionary, pake {}
#Gaboleh ada angka yang sama di dalam set
#biasan
ListContoh_3 = ["z", "f", "c"]
ListContoh_3.sort()
print(ListContoh_3)

_dict = {"hero": "Batman", "level": 55}
print(_dict)
#Bikin program banyak pake dictionary


#Exercise06
#Buat class mobil dengan attribute max_speed dan mileage
#carX = Mobil(240, 18)
#print(carX.max_speed, carX.mileage)
class Mobil:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        print("Instantiate")
    
    #dua method tidak akan dieksekusi sampai dia dipanggil objek
    #method di bawah ini bakal dieksekusi melalui objek
    def getmax_speed(self):
        return self.max_speed
    
    def getmileage(self):
        return self.mileage

#max_speed = ("please input max_speed: ")
#_mileage = ("please input mileage: ")
#carX = Mobil(max_speed, _mileage)
#carX = Mobil(240, 18)

#print(carX.max_speed, carX.mileage)

#Eksekusi sebelum dipanggil

toyota = Mobil(100, 10000)
honda = Mobil(500, 50000)

print(toyota.getmax_speed())
# method constructor
# Kenapa? Karena dia dieksekusi ketika instansiasi terjadi
#Dari kelas diubah jadi objek
#instansiasi = merubah sebuah kelas menjadi sebuah objek
#init akan dieksekusi 
#ada melalui objek
#method nempel ke class bukan ke objek

#Exercise07
#Buat kelas apapun, dengan method yang sama
class Buah:
    def __init__ (self, warna, rasa):
        self.warna = warna
        self.rasa = rasa
        print("Instantiate")

    def getWarna(self):
        return self.warna

    def getRasa(self):
        return self.rasa

apel_malang = Buah("Hijau", "Asam")
pisang = Buah("Kuning", "Manis")

print(pisang.getRasa())

# 1. Klub catur sedang menerima member baru. Syaratnya kalau member berumur lebih dari 30 tahun dan sudah menang 5 piala.
#    Dia akan dimasukkan sebagai member "Profesional". Jika member berusia di bawah 30 tahun kurang dan memiliki piala
#    Kurang dari 5 piala, dimasukkan ke member "Open"
Member_1 = [31, 4] #Hati-Hati Indentasi
_input = [[31, 4], []]
#Umur = Member_1.index(31)
#print(Umur) #keprint indexnya
Umur = Member_1[0]
Piala = Member_1[1]
if Umur > 30 and Piala >=5:
    print("Member_ 1 is Professional.")

else:
    print("Member_1 is Open")

MemberCatur = [[31, 4], [15, 2], [51, 8], [10, 8], [35, 11]]
MemberCatur_Batch02 = [[55, 9], [10, 8], [33, 6], [17, 9]]

def clubCatur(MemberCatur_):
    KualifikasiMember =[]
    for i in MemberCatur_: #i itu index 0 dari MemberCatur, yaitu [31, 4]   
        if i[0] > 30 and i[1] >= 5: #i[0] adalah index pertama dari i
            KualifikasiMember.append("Professional")
    
        else:
            KualifikasiMember.append("Open")
    return KualifikasiMember

print(clubCatur(MemberCatur))
print(clubCatur(MemberCatur_Batch02))

#def clubCat(inpt):
#     return "Pro" if i[0] > 30 else "Open" for i in inpt
#print(clubCat(_input))
#print(Umur)

    #Member_2 = [15, 2]
    #Member_3 = [51, 8]
    #Member_4 = [10, 8]
    #Member_5 = [35, 11]
#def Klub_Catur:
    






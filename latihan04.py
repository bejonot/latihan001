#sort
#merubah urutan bilangan di dalam list
#mengubah secara permanen
listbela = [3,5,2,5,7,8,9,0]
listbela.sort()

_list02 = ["John", "Luke", "Padme"]
_list02.sort()

print(listbela)
print(_list02)

#kita butuh index dari baris bilangan dengan 

#saya mau tahu index dari sebuah value
print(_list02.index("Luke"))

#Menjumlahkan baris data ini
print(sum(listbela))
#Jadi gaperlu looping

#kalau ga pake sum
x = 0
for i in listbela:
    x += i

print(f"sum loop: {x}")
#ini apaan dah f sama {}??? :(((

#ingin menghapus listbela
#gunakan fungsi del untuk menghapus nilai baris dalam list
#del _list02[0] #Pake indexnya yak, bukan valuenya

#remove menggunakan value
_list02.remove("John")
print(_list02)

#Fungsi map
#map(func, iterate) #iterate --> array list
#dia bisa me-- data tanpa looping
#looping tanpa menggunakan for
#map(int, listbela)

#Soal
#def nama_func(): bisa kosong (), atau (a, b)
    #statement

def sum_number(a,b):
    return a + b

print(sum_number(8,9))

# 1389 --> 1 + 3 + 8 + 9 -> 2 + 1 -> 3
#integer gabisa dilooping #'int' object is not iterable #ubahlah int jadi string
def root_number(x):
    z = 0 #diatas? biar ga membawa z ke looping

    for y in str(x): #y akan diasosiasikan dengan variabel x di nilai pertamanya
        z += int(y)
    
    if z > 9:
        z = root_number(z) #manggil diri sendiri, si z yang masih nilainya 2 digit

    return z 

print(root_number(123456789))

def repeat_num(num):
    return num if num < 10 else repeat_num(sum(map(int, str(num))))
    #num diubah pake str
    #dilooping pake map
    #dijumlahin pake sum
    #baca2 lagi tentang map
print(repeat_num(1234))

#Function, menyimpan sebuah fungsi

#Class OOP Object Oriented Program
#class Hero(object):
#class Hero:

class Hero: #yang ada di bawah itu punya class Hero
    # method constructor
    #name dan level disimpan di self.name dan self.level
    #objek hero dalam kelas diubah jadi self
    #self harus ada di dalam method
    def __init__(self, name, level): #self
        self.name = name
        self.level = level 
    #method get name
    #s = 0
    #name = "John Doe"
    def getName(self): 
        return self.name
    
    def getlevel(self):
        return self.level

#Tansformasi kelas menjadi sebuah objek
hero = Hero("One Punchman", "1")
#hero object
#Hero kelas, pindah ke kiri. Hero jadi object

#harus manggil objek(hero) baru tunjuk propertinya(getName)
print(hero.getName())

#class code stater = kelas pembangun

#self?
#java, PHP, membuat self tersurat
#untuk bisa dimanfaatkan, dia memanggil dirinya sendiri, baru dia manggil substansinya
# di luar kelas boleh gausah pake self. karena dia bukan bagian dari kelas.
#def hero():
    #pass
#return artinya mengeluarkan

heroName = hero.getName()
heroLevel = hero.getlevel()
print(f"Hero name is {heroName} and the level is {heroLevel}")

class Calci:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getA(self):
        return self.a
    
    def getB(self):
        return self.b

#angka = Angka(1, 2)
#a = Angka.getA()
#b = Angka.getB()
#print(f"Angka a adalah {a} dan angka b adalah {b}")

#success --> )())())
#hello --> (())(
#def replace_char(word):
    #cek apakah karakter di dalam word memiliki alfabet lebih dari 1, bila iya, print )
    #a = word.count("h")
    #b = word.count("e")
    #c = word.count("l")
    #d = word.count("o")
    #if a,b,c,d > 1:
        #print(")")
    #if a,b,c,d = 1:
        #print("(")

    #cek apakah karakter di dalam word memiliki alfabet 1, bila iya, print (

    pass #buat algoritma



    



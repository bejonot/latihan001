#The "not" operator


#Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

#prints out 3,4,5
#3 start, 10 end
for x in range(3, 6): 
    print(x)

#Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

#While loops
#prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1 #this is the same as count = count + 1
    
#Tugas: Print 3, 6, 9, 12, 15
for x in range(3, 18, 3):
    print(x)

index = 3
while index < 20:
    print(index)
    index += 3

index = 1
while index < 20:
    if index % 3 == 0: #Ketika modulus 3 == 0, berarti si index habis dibagi 3
        print(index)
    index += 1

#Break
#fungsi: nge-cut proses yang berlangsung
# Prints out 0,1,2,3,4
count = 0
while True:
    count += 1
    print(count)
    if count >= 5:
        break

count = 0
while True: #saya punya 0, oke 0 nya true
    print(count) #4 
    count += 1 # 4+1 =5
    if count >= 5: 
        break

#Continue
#Prints out only odd numbers = 1,3,4,7,9
for x in range(10): #Batas rentangnya cuma sampai 10
    #Check if x is even
    if x % 2 == 0: #yang habis dibagi 2 kayaknya 
        continue #balik lagi ke awal
    print(x) #kalau ga pake indentasi, dia masuk ke fungsi if, ga fungsi for

#use "else" in loops
#prints out 1,2,3,4
for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed")

#Exercise 3
#1. Buat baris bilangan genap 1 sampai 10
index = 2
while index < 12:
    print(index)
    index += 2

for x in range(1, 11): #Batas rentangnya cuma sampai 10
    if x % 2 == 1: #sesuatu dibagi dua, modulusnya 1
        continue #balik lagi ke awal
    print(x) #kalau ga pake indentasi, dia masuk ke fungsi if, ga fungsi for

#2. Buat baris bilangan ganjil 1 sampai 10
for x in range(10): #Batas rentangnya cuma sampai 10
    #Check if x is even
    if x % 2 == 0: #yang habis dibagi 2 kayaknya 
        continue #balik lagi ke awal
    print(x) #kalau ga pake indentasi, dia masuk ke fungsi if, ga fungsi for

index = 1
while index < 10:
    print(index)
    index += 2
#For itu digunakan ketika udah punya list
#while itu digunakan dari awal (kayak ngitung baris dan deret)

#Function
def my_function():
    print("Hello from my_function!")
my_function()

def penjumlahan(x,y):
    print(x+y)
penjumlahan(5,12) #memanggil fungsi penjumlahan yang sudah didefinisikan di atas, dengan mengisi x = 5 dan y = 12

def hahahihiye(x,y):
    return x + y #mengembalikan nilai hasil dari dua penjumlahan
#yang direturn bisa kita taro di variabel
yuhu = hahahihiye(1,20)
print(yuhu)

def bilangan3(start,end):
    while start < end:
        if start % 3 == 0:
            print(start)
        start +=1

bilangan3(3,10)

def pythagorass(x,y):
    return (x**2) + (y**2)
sisi_miring = (pythagorass(3,4))**(1/2)
print(sisi_miring)

def showlist(r):
    z = []
    for x in range(r):
        z.append(x)
    return z

d = showlist(20)
print(d)
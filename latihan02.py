listName = ["Anakin Skywalker", "Qui-Gon Jimn", "Ebi Nan Kenoki", "Padme Amidala"]
#print(listName)
#for variable in listName: 
    #print(variable)
print(listName[1])
print(listName[-1])
print(listName[2:3])
print(listName[:3])

#reverse
print(listName[::-1])
listName.reverse()
print(listName)

#number
number = 1 + 2 + 3 / 4.0
print(number)

#modulus
mod = 10 % 3
print(mod)

#pangkat
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#concade
#tambah string + string
helloworld = "hello" + " " + "world"
print(helloworld)

#Using operators with list
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#String Formatting
myString = "Luke Skywalker"
myInt = 12
myFloat = 4.8

# python 2 and > 2
print("My string is %s" % myString)
# %s akan diisi oleh variabel yang paling kanan

print("This is integer number %d" % myInt)
print("The string %s and the integer %d" % (myString, myInt))

#string format
#print("The string format {} and the integer {}".format(myString, myInt))

#reference use index
#print("The string is {0}

#python 3
#print(f"Hello {myString}")

#Basic String Operations
astring = "Hello World!"
print("single quotes are ' '")
print(len(astring))
stringg = "john doe"
print(len(stringg))


#Get use index:
print(astring.index("o")) #lokasi "o" dimana
print(astring.count("l")) #ngitung l ada berapa di "Hello World!"
print(astring[3:7])

#[start:stop:step]
print(astring[3:7:2]) #step 0 2 4 6 8

#reverse
print(astring[::-1])
print(astring.upper())
print(astring.lower())

#cek, hasilnya boolean
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

#split
afewwords = astring.split(" ")
print(afewwords)

#boolean
#isinya cuma dua, True dan False
#logika matematika
# True    True    True
# False   True    False
# True    False   False
# False   False   False

#Conditions
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3)  # prints out True

#Boolean Operators
name = "John"
age = 23
#condition harus true jika statement dieksekusi, kondisi harus terpenuhi
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

#The "In" Operator
name = "Luke"
if name in ["Luke", "Han"]:
    print("Your name is either Luke.")

#if and else
diajahat = False
diabaik = True
if diajahat is True:
    # do something
    print("Dia bukan jodohku :(")
    pass
elif diabaik is True: #else if
    #do something else
    print("Dia jodohku :3")
    pass
else:
    #do another thing
    print("Dia gajelas :/")
    pass

#The "is" operator:
z = [1,2,3]
y = [1,2,3]
print(z == y) # Prints out True
print(z is y) # Prints out False
w = z
print(w is z) # Prints out True
#is akan membandingkan instansiasinya, bukan valuenya
# == membandingkan valuenya

# === artinya membandingkan value dan tipe data, tapi di python gaada, === invalid syntax
g = 3
o = "3"
print(g == o)
#ingatkan jelaskan

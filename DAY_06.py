#strings

name = 'NETHRA ELNA RAJU'
sem = 'FIRST SEMESTER'
course = 'BCA FS'

print()
print("-----------STUDENT DETAILS----------")
print(f"NAME OF THE STUDENT : {name}")
print(f"SEMESTER OF EXAM    : {sem}")
print(f"COURSE DETAILS      : {course}")
print('------------------------------------')
print()

#concatination
print("CONCATINATION OF STRING")
print('-' * 30)
a = "APPLE"
b = 'MANGO'
c = a + b
print(f"EXCLUDUNG SPACE : {c}")     # -------> concatnation of 2 string 
print(f"INCLUDING SPACE : {a + ' ' + b}")
print()


#indexing
print("INDEXING")
print('-' * 30)
print(name[4])      # ----------> NETHRA ELNA RAJU 
print(name[7])
print(name[-5])
print(name[-3])
print()

#slicing 
print("SLICING")
print('-' * 30)
print(name[::-1])
print(name[5:-8])
print(name[-8:])
print(name[::2])
print()

#string methods 
print("STRING METHODS")
print('-' * 30)
print(f"THE LENGHT OF {name} IS : {len(name)}")
print(f"REPLACE 'A' WITH @ : {name.replace('A','@')}")
print(f"FINDING : {name.find('E')}")
words = name.split()
print(f"THE SPLITED WORDS ARE : {words}")      # ------> return in form of list
print('^'.join(name))
print()

if name.startswith("N") and name.endswith('U'):
    print("STARTS WITH N AND ENDS WITH U")
print()

#case changing methods
print(f"UPPERCASE : {name.upper()}")   # -----> to make name in uppercase
print(f"LOWERCASE : {name.lower()}")   # -----> to make name in lowercase
print(f"CAPITALIZE : {name.capitalize()}")
print(f"SWAPCASE : {name.swapcase()}")
print()

#program
print('-' * 30)
sentence = input("ENTER : ")
if sentence.isdigit():
    print("CONTAINS ONLY DIGITS ")
#elif sentence.isalnum():
 #   print("HAS BOTH NBR AND ALPHA")
elif sentence.isupper():
    print("STRINGS ARE IN UPPERCASE")
elif sentence.islower():
    print("STR IN LOWERCASE")
elif sentence.isascii():
    print("CONTAINS SPECIAL TRAIT")
elif sentence.isalpha() and  sentence.isupper():
    print("UPPERCASE WITH ALPHABETS ONLY !!")
elif sentence.isalpha() and  sentence.islower():
    print("LOWERCASE WITH ALPHABETS ONLY !!")
else:
    print("Oops ntg!!")
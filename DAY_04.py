#string method

name = input("ENTER UR NAME : ")
n = len(name)
print(f"LENGHT OF {name} IS {n}")


print(name.find(" "))  #find element
print(name.capitalize())   #to captialize the 1st letter

if name.isupper():
    print("NAME IS IN UPPER CASE")
elif name.islower():
    print("NAME IS IN LOWER CASE")
elif name.isalpha():
    print("ONLY ALPHABETS")
else:
    print("NONE")

print("---------------------------------------------------")
email = input("ENTER THE EMAIL ID  : ")
i = email.index("@")
username = email[:i]
domain = email[i:]
print()
print(f"YOUR USERNAME IS {username} AND DOMAIN IS {domain}")

print()
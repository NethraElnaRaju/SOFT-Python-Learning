#operations 

print()
print("--------SIMPLE CALCULATER----------")
print()
num1 = eval(input("ENTER THE NUMBER 1 : "))
ch = input("EITHER (+,-,/,*) : ")
num2 = eval(input("ENTER THE NUMBER 2 : "))

print()
if ch == '+':
    r = num1 + num2
    print(f"RESULT OF {num1} + {num2} IS {r}")
elif ch == '-':
    r = num1 - num2
    print(f"RESULT OF {num1} - {num2} IS {r}")
elif ch == '*':
    r = num1 * num2
    print(f"RESULT OF {num1} * {num2} IS {r}")
elif ch == '/':
    r = num1 / num2
    print(f"RESULT OF {num1} / {num2} IS {r}")
else:
    print("INVAILD CHOICE ENTERED !!")
print()
print("-------------------------------------")  
    
    
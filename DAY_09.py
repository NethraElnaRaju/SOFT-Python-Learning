# simple calculater

print("------------SIMPLE CALCULATER-----------\n")
while True:
    a = eval(input("ENTER THE NBR 1 : "))
    ch = input("ENTER (+,-,/,*) : ")
    b = eval(input("ENTER THE NBR 2 : "))
    
    if ch == '+':
        result = a + b
        print()
        print(f"RESULT OF {a} + {b} IS : {result}")
    elif ch == '-':
        print()
        print(f"RESULT OF {a} - {b} IS : {a - b}")
    elif ch == '/':
        print()
        if b!=0:
           print(f"RESULT OF {a} / {b} IS : {a/b}")
        else:
            print("DIVISION BY ZERO")
    elif ch == '*':
        print()
        print(f"RESULT OF {a} * {b} IS : {a*b}")
    else:
        print()
        print("INVAILD CHOICE")
    print()
    do = input("CONTINUE ?? (Y/N)").upper()
    if do == 'N':
        print("THANK YOU")
        break
    print('---------------------------------------')
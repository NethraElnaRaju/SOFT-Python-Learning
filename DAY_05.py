#list

while True:
    print("--------------------------------------")
    print("A --> LIST OF NBR")
    print("B --> LIST OF FRUITS")
    ch = input("ENTER (A/B) : ").upper()
    print("--------------------------------------")
    print()

    if ch == 'A':
        l=[]
        limit = eval(input("ENTER THE LIMIT :  "))
        for x in range(limit):
            num = eval(input(f"ENTER THE NUMBER {x+1} : "))
            l.append(num)

        print()
        print(f"THE LIST CONTAINS : {l}")
        print()

        #list operations 
        print(f"LENGTH OF LIST : {len(l)}")    # --------> to print length of list

        a = 12
        l.append(a)
        print(f"APPENDED 12 TO LIST : {l}") #--------> to append an item at end
        print()

        l.remove(12) # --------> to remove element
        print(f"REMOVED 12 : {l}")
        print()

        l.insert(1,23)  # -------> to insert to a specific position 
        print(f"INSERT TO A SPECIFIC POSITION : {l}")
        print()

        if len(l)>=2:  # -------> to update a element 
            l[1] = 123
        else:
            l[0] = 321

        print("-----UPDATED LIST -----")
        print(l)
        print()

        #searching and counting
        x = eval(input("ENTER THE NBR WITHIN THE LIST TO SEAECH  : "))
        print(f"{x} is in index of :  {l.index(x)}") # ------> if element not present its a error
        print(f"THE COUNT OF {x} IS : {l.count(x)}")
        print()

    elif ch == 'B':
        #list slicing 
        fruits = ['APPLE','BANANA','MANGO','CHERRY','PAPAYA','STRAWBERRY','KIWI','WATERMELON']
        print(fruits[0])
        print(fruits[1:4])
        print(fruits[::-1])
        print(fruits[::2])
        print(fruits[-6:])

        #sort and reverse
        fruits.sort()   # ------> from A-Z sorting 
        print(fruits)
        fruits.sort(reverse=True)
        print(fruits)
    else:
        print("INVAILD CHOICE !!")
    do = input("CONTINUE (Y/N) : ").upper()
    if do == 'N':
        break
# tuple = ()  ordered and unchangeable (immutable)
# tuple is faster than list

print("______________________________________")
print()
print("| 1 ---> ADD ELEMENT IN TUPLE        |")
print("| 2 ---> WEEKLY WORKOUT LIST         |")
print("| 3 ---> STUDENT MARK ANALYSIS       |")
print("______________________________________")
print()
while True:
    choice = eval(input("ENTER THE CHOICE  : "))
    if choice == 1:
        t = ()
        limit = eval(input("ENTER THE LIMIT  : "))
        for x in range(limit):
            element = eval(input(f"ENTER THE NBR{x+1}  : "))
            t+=(element,)
        print(f"TUPLE OF NBR : {t} \n")

        # The 2 methods in tuple

        print("------------TUPLE METHODS---------------")
        if 10 in t:
            print(f"INDEX OF 10 IS : {t.index(10)}")
        else:
            print("10 is not present in the tuple")
        search = eval(input("ENTER THE NBR TO COUNT  : "))
        print(f"COUNT OF {search} IS : {t.count(search)}")

    elif choice == 2:
        # workout program 
        print("<---------------WEEKLY WORKOUT TIMETABLE-------------------------->\n")
        workout = ("Running","Cycling","Yoga","Running","Swimming","Yoga","Running")
        print(workout)   # -----> to display 
        print()
        run = workout.count("Running")
        print(f"OCCURANCE OF RUNNING IS {run}")

        index_of = workout.index("Swimming")
        print(index_of)   # ----> index of 

        ask = input("ENTER A WORKOUT : ")
        print(workout.count(ask))

    elif choice ==3:
        #students mark analysis
        marks = (85, 90, 75, 90, 60, 85, 90)
        print("MARKS IS : ",marks)
        print(f"OCCURANCE OF 90 IS : {marks.count(90)}")
        print(f"1ST OCCURANCE OF 85 IS : {marks.index(85)}")
        ask_mark = eval(input("ENTER THE MARK TO COUNT  : "))

        if ask_mark in marks:
            print(f"OCCURANCE OF {ask_mark} IS : {marks.count(ask_mark)}")
        else:
            print("MARK NOT FOUND !!")
    else:
        print("INVAILD CHOICE !! ")
    do = input(" DO U WANT TO CONTINUE (Y/N): ").upper()
    if do == 'N':
        break
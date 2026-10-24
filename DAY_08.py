# set ---> no duplicate allowed

while True:
    print("1 ---> SET")
    print("2---> DICT")
    print("3 ---> PROGRAM")
    ch = eval(input("CHOICE : (1/2/3) : "))
    if ch == 1:
        num = {10,20,30,50,40,20,10}    # ----> unordered
        print()
        print("-----------------SET-----------------\n")
        print(f"THE SET CONTAINS : {num}")
        a = {"Eng", "Maths", "Python"}
        b = { 20,40,50,60}
        union = a | num
        print()
        print(f"UNION OF {a} AND {num} IS : {union}")
        inter = a & num
        print()
        print(f"INTERSECTION OF {a} AND {num} IS : {inter}")
        a.add("C++")
        print(f"NEW SET IS {a}")
        print()
    elif ch == 2: 
        # dictionary
        print("-----------------DICTIONARY-------------------\n")
        student = {"name": "Nethra","age": 18,"course": "BCA","mark": 85}
        print(student)

        print(student['name'])   # --------> to acess value
        print(student['age'])
        print(student.get("name"))

        student['name'] = "GARBIELLA"  # ----> to update a dict
        del student['mark']  # --------------> to del both key and values
        print(student)

        print(f"KEYS IN STUDENT : {student.keys()}")
        print(f"VALUES IN STUDENT : {student.values()}")
        print(f"KEY - VALUE : {student.items()}")
        student.pop('age')
        print(student)
        student.popitem()  # ----> to del last entry
        print()
    elif ch == 3:
        #Student Marks Management
        print("--------------PROGRAM----------------------\n")
        marks = { "Arun": 78, "Meera": 92, "Rahul": 65, "Anu": 88, "Kiran": 74}
        for x,y in marks.items():
            print(x,y)

        marks["GARBIELLLA"] = 99
        print(f"NAME ADD TO DICT : {marks}")
        marks["Rahul"] = 78
        print(f"UPDATED TO DICT : {marks}")

        print(max(marks.values()))
    else:
        print("INVAILD CHOICE")
    do = input("CONTINUE (Y/N) : ").upper()
    if do =='N':
        break
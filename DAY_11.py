# functions 

# Function without parameters
print()
print("Function without parameters")
def sum():
    a = eval(input("ENTER THE NBR 1 : "))
    b = eval(input("ENTER THE NBR 2 : "))
    c = a + b
    print(f"SUM OF 2 NBR IS : {c}\n")
sum()

# Function with parameters
print("Function with parameters")
def add(a , b):
    c = a + b
    print("SUM OF NBR IS : ",c)
a = eval(input("ENTER THE NBR 1 : "))
b = eval(input("ENTER THE NBR 2 : "))
add(a , b)  
print()

# Function with return
print("Function with return")
def sum():
    a = eval(input("ENTER THE NBR 1 : "))
    b = eval(input("ENTER THE NBR 2 : "))
    c = a + b
    return c
call = sum()
print(call)
print()

# calculater
print("CALCULATER")
def cal(x , y):
    add = x+y
    sub = x-y
    mul = x*y
    div = x/y
    return add , sub , mul , div

x = eval(input("ENTER THE NBR 1 : "))
y = eval(input("ENTER THE NBR 2 : "))
print(cal(x,y))

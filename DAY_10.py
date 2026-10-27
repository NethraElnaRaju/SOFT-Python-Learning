#Using a while loop 
##Write a program to print all even numbers from 2 to 20.

print("EVEN NBR\n")
n = 2
while n<=21:
    print(n)
    n+=2

#multiplication table 
#for loop

print("MULTIPLICATION TABLE\n")
num = eval(input("ENTER THE NBR : "))
for x in range(1,11):
    print(f"{num} x {x} = {num*x}")

#break
while True:
    nbr = eval(input("ENTER THE NBR : "))
    if nbr == 0:
        print("YOU ENTERED ZERO   ----->  EXIT ")
        break
    
#sum of digit 
ask = eval(input("ENTER THE NBR : "))
r = 0
while ask!=0:
    r += ask % 10
    ask = ask//10
print(r)

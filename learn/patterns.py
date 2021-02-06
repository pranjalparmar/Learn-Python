num = int(input("Enter the number= \n"))
x = int(input("Enter 0 or 1 \n"))
a = bool(x)
if a==1:
    for i in range(num):
        for j in range(1,i+2):
            print("*", end = " ")
        print()
if a==0:
    for i in range(num):
        for j in range(1,num-i+1):
            print("*", end=" ")
        print()
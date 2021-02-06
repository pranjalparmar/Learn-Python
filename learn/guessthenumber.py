import random
n = random.randint(1,100)
b = int(input("Enter the no. of guesses"))
print("enter the value")
for i in range(1,100):
    for i in range(b):
        a = int(input())
        if a<n:
            print("choose higher value")
        elif(a==n):
            print("Well Done!", "you guessed it correctly in ",(i+1),"attempts")
            break
        elif(a>n):
            print("choose lower number")
        print("number of guesses left=",b-i-1)
    break
print("game is over")
print("the correct value was ",n)

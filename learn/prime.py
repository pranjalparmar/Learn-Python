a = int(input("Enter the number you want to check for = "))

for i in range(2,a/2):
    if a % i == 0:
        print("Is not a prime number")
        break
else:
    print("is a prime number")
n=int(input())
for i in range(1,3*(n+1)):
    if i%3 == 0:
        print("*****")
    else:
        print("*   *")
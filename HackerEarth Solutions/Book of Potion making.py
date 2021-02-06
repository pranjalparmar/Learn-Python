t = input()
a = 0
if len(t)==10:
 
    for i in range(1,11):
        z = int(t[i-1])*i
        a += z
 
    if a % 11 == 0:
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
 
else:
    print("Illegal ISBN")
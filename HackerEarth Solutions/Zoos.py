import sys
a = input()
x = 0
y = 0
if len(a) <= 20:
    for i in a:
        if i == 'z':
            x+=1
        else:
            y+=1
    
    if 2 * x == y:
        print("Yes")
    else:
        print("No")
else:
    sys.exit()
import sys
 
n = int(input())
 
if n <= 10000:
    c = 0
 
    for i in range(1,10001):
        a = i
        b = 2*i
        count = a+b
        c += count
 
        if c >= n :
            break
 
    if  n > c - b:
        print("Motu")
    else:
        print("Patlu")
 
else:
    sys.exit()
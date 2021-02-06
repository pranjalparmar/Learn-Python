import sys
s = input()
if len(s) <= 1000:
    x = s.split()
    a = x[::-1]
 
    for i in a:
        print(i,end=" ")
else:
    sys.exit()
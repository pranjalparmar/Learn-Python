import sys
t = int(input())
x=0
for i in range(t):
    n = int(input())
    j=0
    while(x==1):
        if n % 2 == 0:
            x=n/2
        else:
            x=(3*n)+1
        j+=1
 
    print('YES')
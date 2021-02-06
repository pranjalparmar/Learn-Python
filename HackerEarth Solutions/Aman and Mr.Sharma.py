d = int(input())
 
t = 0
 
for i in range(d):
        r,x = list(map(int,input().split()))
 
        if (44*r)/7<100*x:
                t+=1
 
print(t)
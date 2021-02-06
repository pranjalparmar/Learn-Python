a = int(input())
b = list(map(int, input().split()))
lst=[]
for i in range(a):
    data=b[i]%10
    lst.append(data)
s = ''.join(map(str, lst))
 
if int(s) % 10 == 0:
    print('Yes')
else:
    print('No')
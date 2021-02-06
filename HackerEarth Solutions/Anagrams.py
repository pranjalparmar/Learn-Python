import sys
from collections import Counter
test = int(input())
for j in range(test):
    a = input()
    b = input()
 
if len(a)<=10000 and len(b)<=10000:
 
    x = len(a) + len(b)
    d1 = Counter(a)
    d2 = Counter(b)
 
    df = d1 & d2
 
    values = df.values()
    z=0
    for i in values:
        z+=i
 
    t = x - 2*z
    print(t)
else:
    sys.exit()
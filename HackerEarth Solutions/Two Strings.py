from itertools import permutations
y = int(input())
for i in range(y):
    s1,s2 = input().lower().split()
    
    if sorted(s1) == sorted(s2):
        print('YES')
    else:
        print('NO')
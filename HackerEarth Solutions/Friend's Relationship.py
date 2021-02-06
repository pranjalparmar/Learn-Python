t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        for k in range(2*n):
            if k<=j:
                print('*',end='')
            elif k+j >= 2*n-1:
                print('*',end='')
            else:
                print('#',end='')
        print()
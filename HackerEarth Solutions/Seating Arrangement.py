import sys
T = int(input())
 
if T <= 10**5:
    for i in range(T):
        N = int(input())
        if N >= 1 and N <=108:
            z = N % 12
 
            if z == 1 or z == 6 or z == 7 or z == 0:
                if z == 1:
                    print(N+11,"WS")
                elif z == 6:
                    print(N+1,"WS")
                elif z == 7:
                    print(N-1,"WS")
                else:
                    print(N-11,"WS")
 
            elif z == 2 or z == 5 or z == 8 or z == 11:
                if z == 2:
                    print(N+9,"MS")
                elif z == 5:
                    print(N+3,"MS")
                elif z == 8:
                    print(N-3,"MS")
                else:
                    print(N-9,"MS")
 
            else:
                if z == 3:
                    print(N+7,"AS")
                elif z == 4:
                    print(N+5,"AS")
                elif z == 9:
                    print(N-5,"AS")
                else:
                   print(N-7,"AS")
        else:
            sys.exit()           
else:
    sys.exit()
t = int(input())
for i in range(t):
    sh,sm,eh,em = list(map(int,input().split()))
 
    sm = 60 - sm
 
    if (sm+em)/60 < 1:
        print(eh - sh - 1, sm+em)
    else:
        print(eh - sh, (sm+em)%60)
L = int(input())
N = int(input())
  
for i in range(N):
    wh = input().split()
    W = int(wh[0])
    H = int(wh[1])
 
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W==H:
        print("ACCEPTED")
    else:
        print("CROP IT")
    
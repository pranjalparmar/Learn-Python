n = int(input())
z = input().upper()
if "HH" in z:
    print("NO")
else:
    print("YES")
    print(z.replace('.','B'))
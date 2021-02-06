from array import *

arr = array('i',[])

n = int(input("Enter the size of the array:\n"))

for i in range(n):
    val = int(input("Enter the value:\n"))
    arr.append(val)

print(arr)
z = int(input("Enter the value you want know the index for"))
k=0
for e in arr:
    if e == z:
        print(k)
        break
    k+=1

print(arr.append(z))
# for i in range(4):
#     for j in range(4):
#         if j<=i:
#             print(chr(65+j), end=" ")
#         else:
#             print(chr(79+j),end=" ")
#     print()


# for i in range(1,5):
#     for j in range(1,6-i):
#       print(i+j-1,end=" ")
#     print()


# i=1
# while i<=4:
#     print("#",end="")
#
#     j=1
#     while j<=5:
#         print("#",end="")
#         j+=1
#     print()
#     i+=1


# for i in range(1,501):
#     if i**2 in range(501):
#         print(i**2)


# for letter in character_range('a', 'z'):
#     print( chr(letter), end=", " )



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


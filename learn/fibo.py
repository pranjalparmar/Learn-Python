
# def fibon():
#     a = 0
#     b = 1
#     n = int(input("Enter the number = \n"))
#     for i in range(0,n):
#         c = a + b
#         a = b
#         b = c
#         print(c)
#
# fibon()

# def fibon():
#     a = 0
#     b = 1
#     c = 0
#
#     n = int(input("Enter the number = \n"))
#
#     if n == 1:
#         print(a)
#
#     else:
#
#         print(a)
#         print(b)
#
#         while c<n:
#             c = a + b
#             a = b
#             b = c
#
#             if c>n:
#                 break
#
#             print(c)
#
# fibon()

# def fact(n):
#
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
#
# n = int(input("Enter the number:\n"))
# result = fact(n)
# print(result)

f = lambda a,b : a+b
result = f(5,6)
print(result)
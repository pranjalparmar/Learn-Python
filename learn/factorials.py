n = int(input("Enter the number = "))


def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(n))


# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(n))
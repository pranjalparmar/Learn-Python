# score = float(input("Enter Score: "))

# if score <= 1.0:
#     if score >= 0.9:
#         print("A")
#     elif score >= 0.8:
#         print("B")
#     elif score >= 0.7:
#         print("C")
#     elif score >= 0.6:
#         print("D")
#     else:
#         print("F")
# else:
#     print("Error")


def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay = (40 * r) + ((h - 40)*(1.5*r))

    return pay


h = int(input())
r = float(input())
p = computepay(h, r)
print("Pay", p)

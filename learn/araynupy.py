from numpy import *

# arr = array([1,2,3,4,5,6])
#
# #Using of linspace()
#
# arr1 = linspace(1,15,20)
# #range goes from 1 to 15 aand divides it into 20 parts
#
# arr2 = logspace(1,15,16)
#
# arr3 = arange(1,15,2)
#
# print(arr3)

arr1 = array([
                [1,5,3],
                [5,6,3],
                [2,6,3]

            ])
#
# arr2 = arr1.flatten()
#
# arr3 = arr2.reshape(2,2,3)

m = matrix(arr1)
print(m.max())
print(diagonal(m))
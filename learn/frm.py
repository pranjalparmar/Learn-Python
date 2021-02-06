from functools import reduce

nums = ['1','3','4','3','7','6']

evens = list(filter(lambda n : int(n)%2==0, nums))

doubles = list(map(lambda n : int(n)*2, nums))

reduces = reduce(lambda a,b: int(a) + int(b), nums)

print(reduces)

### Roy and profile picture
# L = int(input())
# N = int(input())
# i = 0
#
# while i <= N:
#     wh = input().split()
#     W = int(wh[0])
#     H = int(wh[1])
#
#     if W < L or H < L:
#         print("UPLOAD ANOTHER")
#     elif W >= L and int(H) >= L:
#         if W == H:
#             print("ACCEPTED")
#         else:
#             print("CROP IT")

### Anagrams
import sys
from collections import Counter
#
# test = int(input())
# a = input()
# b = input()
#
# x = len(a) + len(b)
# # y = ""
# for i in a:
#     if i in b:
#         y+=i
#
# z = x - 2*len(y)
# print(z)
# Dict1 = Counter(a)
# Dict2 = Counter(b)
#
# q = Dict1 & Dict2
# print(q)
#
# values = q.values()
# z=0
# for i in values:
#     z+=i
#
# print(z)
#
# print(values)

# set( Dict1.items() ) & set( Dict2.items() )
# # if len(a) <= 10000 and len(b) <= 10000:
#
#
#
# print(x)
# print(y)


### Seating Arrangement

# import sys
# T = int(input())
#
# if T <= 10**5:
#     for i in range(T):
#         N = int(input())
#         if N >= 1 and N <=108:
#             z = N % 12
#
#             if z == 1 or z == 6 or z == 7 or z == 0:
#                 if z == 1:
#                     print(N+11,"WS")
#                 elif z == 6:
#                     print(N+1,"WS")
#                 elif z == 7:
#                     print(N-1,"WS")
#                 else:
#                     print(N-11,"WS")
#
#             elif z == 2 or z == 5 or z == 8 or z == 11:
#                 if z == 2:
#                     print(N+9,"MS")
#                 elif z == 5:
#                     print(N+3,"MS")
#                 elif z == 8:
#                     print(N-3,"MS")
#                 else:
#                     print(N-9,"MS")
#
#             else:
#                 if z == 3:
#                     print(N+7,"AS")
#                 elif z == 4:
#                     print(N+5,"AS")
#                 elif z == 9:
#                     print(N-5,"AS")
#                 else:
#                    print(N-7,"AS")
#         else:
#             sys.exit()
# else:
#     sys.exit()

### Print numbers

# for num in range(ord("#"), ord("V")):
#     print(num - ord("#"),)

# for i in range(1, 255):
#     ch = chr(i);
#     print(i, "=", ch);

### Brick Game
# n = int(input())
# c = 0
#
# for i in range(1,10001):
#     a = i
#     b = 2*i
#     count = a+b
#     c += count
#
#     if c >= n :
#         break
#
# if  n > c - b:
#     print("Motu")
# else:
#     print("Patlu")

### Print Numbers:

# n = int(input())
# arr = list(map(int,input().split()))[:n]
# for i in range(n-1):
#     print(arr[i], end='-')
# print(arr[n-1],"\n")


### Two Strings:
from itertools import permutations

# y = int(input())
# for i in range(y):
#     s1, s2 = input().lower().split()
#
#     if sorted(s1) == sorted(s2):
#         print('YES')
#     else:
#         print('NO')


###
#
# t = input()
# a = 0
# if len(t)==10:
#
#     for i in range(1,11):
#         z = int(t[i-1])*i
#         a += z
#
#     if a % 11 == 0:
#         print("valid isbn")
#     else:
#         print("illegal isbn")


###

# s = input()
# z = 0
#
# for i in range(len(s)):
#     z += ord(s[i])-96
#
# print(z)
#

###

# s = input()
#
# x = s.split()
# a = x[::-1]
#
# for i in a:
#     print(i,end=" ")

###
# t = int(input())
# for i in range(t):
#     sh,sm,eh,em = list(map(int,input().split()))
#
#     sm = 60 - sm
#
#     if (sm+em)/60 < 1:
#         print(eh - sh - 1, sm+em)
#     else:
#         print(eh - sh, (sm+em)%60)

###

# a = int(input())
# b = list(map(int, input().split()))
# lst=[]
# for i in range(a):
#     data=b[i]%10
#     lst.append(data)
# s = ''.join(map(str, lst))
# print(s)
#
# if int(s) % 10 == 0:
#     print('Yes')
# else:
#     print('No')

###
# n = int(input())
# x = int((n/5))+1
# if n%5 == 0:
#     print(x-1)
# elif n%5 == 1:
#     print(x)
# elif n%5 == 2:
#     print(x)
# elif n%5 == 3:
#     print(x)
# else:
#     print(x)

###

# t = int(input())
#
# for i in range(t):
#     n = int(input())
#
#
#     for j in range(100000000):
#         count = 0
#         if n % 2 == 0:
#             count=n/2
#         else:
#             count=(3*n)+1
#         if count==1:
#             break
#     if count==1:
#         print('YES')
#     else:
#         print('NO')
#


########

# n = input().upper()
# lst = ['A','E','I','I','O','U','Y']
# dig = []
#
# for i in range(1,9):
#     if n[i].isdigit() and n[i-1].isdigit():
#         z = int(n[i])+int(n[i-1])
#         if z % 2 == 0:
#             dig.append('valid')
#         else:
#             dig.append('invalid')
#     if n[i].isalpha():
#         if n[i] in lst:
#             dig.append('invalid')
#         else:
#             dig.append('valid')
# y = set(dig)
# if 'invalid' in y:
#     print('invalid')
# else:
#     print('valid')


######

# n=int(input())
# for i in range(1,3*(n+1)):
#     if i%3 == 0:
#         print("*****")
#     else:
#         print("*   *")

#######
# n = int(input())
# z = input().upper()
# y = [char for char in z]
# for i in range(len(z)):
#     if y[i]=='H':
#         if y[i-1]!='H':
#             print('YES')
# print(z.replace('.','B'))

##########

import sys
# t = int(input())
# x=0
# for i in range(t):
#     n = int(input())
#     j=0
#     while(x==1):
#         if n % 2 == 0:
#             x=n/2
#         else:
#             x=(3*n)+1
#         j+=1
#
#     print('YES')

# #############
#
# n=int(input())
#
# for i in range(n):
#
#     ne=int(input())
#
#     re=ne
#
#     while re>=2:
#
#         if re % 2 == 0:
#
#             re = re // 2
#
#         elif re % 2 != 0:
#
#             re = (3 * re) + 1
#
#         if re==1:
#
#             print('YES')

###############3


# n,q = list(map(int,input().split()))
# arr = list(map(int,input().split()))
# for i in range(q):
#     l,r = list(map(int,input().split()))
#     x = arr[l - 1:r]
#     print(sum(x) // len(x))

# try:
#     age = int(input('Age:'))
#     print(age)
# except ValueError:
#     print('Invalid Value')

#############################

# N = int(input())
# if N % 2 != 0:
#     print('Weird')
# elif N > 1 and N < 6:
#     print(' Not Weird')
# elif N > 5 and N < 21:
#     print('Weird')
# else:
#     print('Not Weird')

#
# n = int(input())


#
# for i in range(n):
#     S = input()
#     o = []
#     e = []
#     O = ''
#     E = ''
#
#     for i in range(len(S)):
#
#         if i % 2 == 0:
#             e.append(S[i])
#
#         else:
#             o.append(S[i])
#
#     a = O.join(o)
#     b = E.join(e)
#
#     print(b," ",a)



####################

# t = int(input())
#
# a = ['a', 'e', 'i', 'o', 'u']
#
# for i in range(t):
#     b = 0
#     n = int(input())
#     s = input()
#
#     for j in range(len(s)):
#         if s[j] in a:
#             if s[j - 1] not in a:
#                 b += 1
#
        # else:
        #     if s[j + 1] in a:
        #         b += 1
        # print(b)

# t = int(input())
# a = ['a','e','i','o','u']
# for i in range(t):
    # b = 0
    # n = input()
    # s = input()
    #
    # for j in range(len(s)-1):
    #     if s[0] in a:
    #        if s[j] not in a:
    #            if s[j+1] in a:
    #                b+=1
    #     else:
    #         if s[j + 1] in a:
    #             b += 1
    #
    #
    # print(b)


##############
# name = input("Enter file:")
# if len(name) < 1: name = "mbox-short.txt"
# import collections
# handle = open('mbox-short.txt')
#
# lst = []
# list = []
# counts = dict()
# for line in handle:
#     if line.startswith('From'):
#         if line.startswith('From:'):
#             continue
#         else:
#             lst = line.rstrip().split()
#
#         a = lst[5].split(':')
#         list.append(a[0])
# list.sort()
# Counter = collections.Counter(list)
#
# for i,h in Counter.items():
#     print(i,h)

#
# for word in list:
#     counts[word] = counts.get(word, 0) + 1
#
# print(counts)

# maxi = max(counts, key = counts.get)
# print(maxi)
#
# for i in counts:
#     if i == maxi:
#

# bigcount = None
# bigword = None
#
# for word,count in counts.items():
#     if bigword is None or count > bigcount:
#         bigword = word
#         bigcount = count
#
# print(bigword,bigcount)
#
# for count in counts.values():
#     if bigcount is None or count > bigcount:
#         bigcount = count






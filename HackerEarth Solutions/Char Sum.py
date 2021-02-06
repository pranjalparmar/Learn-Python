s = input()
z = 0
 
for i in range(len(s)):
    z += ord(s[i])-96
 
print(z)
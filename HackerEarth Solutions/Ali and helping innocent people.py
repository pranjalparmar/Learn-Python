n = input().upper()
lst = ['A','E','I','I','O','U','Y']
dig = []
 
for i in range(1,9):
    if n[i].isdigit() and n[i-1].isdigit():
        z = int(n[i])+int(n[i-1])
        if z % 2 == 0:
            dig.append('valid')
        else:
            dig.append('invalid')
    if n[i].isalpha():
        if n[i] in lst:
            dig.append('invalid')
        else:
            dig.append('valid')
y = set(dig)
if 'invalid' in y:
    print('invalid')
else:
    print('valid')
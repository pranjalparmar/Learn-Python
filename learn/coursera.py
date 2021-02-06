import re

fh = open("actual.txt",'rt')
lst = []
listadd = []
add = 0
for line in fh:
    for word in line.split():
        f = re.findall('[0-9]+',word)
        lst.append(f)
for i in lst:
    for j in i:
        add+=int(j)

print(add)


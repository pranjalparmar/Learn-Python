print('ENTER A NUMBER')
n = int(input())
print('PRIME NUMBERS TILL', n ,'are...')
for i in range(2,n+1):
	for j in range(2,i):
		if i%j == 0:
			break
	else:
		print(i)
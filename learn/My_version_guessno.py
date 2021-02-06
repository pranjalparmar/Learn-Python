n = 13
print('IN HOW MANY ATTEMPTS YOU CAN GUESS A GIVEN NUMBER?')
j = int(input())
for i in range(j):
	print('YOU HAVE ', j-i ,' GUESSES LEFT')
	print('ENTER A VALUE')
	a = int(input())
	if a<n:
		print("CHOOSE A HIGHER VALUE")
	elif a==n:
		print("WELL DONE!")
		print('YOU GUESSED IT CORRECTLY IN ', i+1,' ATTEMPTS')
		break
	else:
		print("CHOOSE A LOWER NUMBER")
print('GAME OVER')
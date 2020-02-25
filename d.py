country = input('Which country are you from?')
age = input('How old are you?')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You are able to drive!')
	else:
		print('You are not allowed to drive!')
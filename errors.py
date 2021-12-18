# 1. Oprava kodu
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print('My favorite season is', seasons[4])
print('My favorite season is', seasons[3])
print('My favorite season is', seasons[len(seasons) - 1])

# 2. Oprava kodu
message = 'The rythm of waltz is: '
a = ' DA'
b = ' da'
for number in range(10):
	# if (Number % 3 ) == 0:
	if (number % 3) == 0:
		message = message + a
	else:
		# message = message + 'b'
		message = message + b
print(message)

# 3. Dotaz na uzivatelske jmeno
class NumberInUsername(Exception):
	pass
class SpacesInUsername(Exception):
	pass
class UsernameNotCapitalized(Exception):
	pass

user_name = input('Your name? ')
try:
	string_list = list(user_name)
	space = ' '
	numbers_in_name = [i for i, letter in enumerate(string_list) if letter.isdigit()]
	if len(numbers_in_name) > 0:
		raise NumberInUsername
	if space in string_list:
		raise SpacesInUsername
	if string_list[0].islower():
		raise UsernameNotCapitalized
except NumberInUsername:
	print(('Username contains numbers'))
except SpacesInUsername:
	print('Username contains spaces')
except UsernameNotCapitalized:
	print("Username doesn't start with capital letter") 
else:
	print("Everything's OK")

# 4. Deleni cisel
def divide():
	while True:
		dividend = input('Enter dividend ')
		if dividend.isdigit():
			break
	while True:
		divisor = input('Enter divisor ')
		if divisor.isdigit() and int(divisor) == 0:
			print("Divisor can't be equal to zero")
		if divisor.isdigit() and int(divisor) != 0:
			break
	return int(dividend) // int(divisor)
print('The result of division is', divide())

# 5. Debugovani
try:
	year = int(input('Greetings! What is your year of origin? '))
except ValueError:
	print('This is not a year')
else:
	if year <= 1900:
		print("Woah, that's the past!")
	elif year > 1900 and year < 2020:
		print("That's totally the present!")
	else:
		print("Far out, that's the future!!")

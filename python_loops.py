# 1. seznamy
name_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef', 'Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal', 'Lenka', 'Katerina']
user_name = input('Your name? ')
if user_name in name_list:
	print('Hello {0}'.format(user_name))
else:
	print("Sorry, we don't know such a name. Are you Czech at all?")

# Smycky
d = {
	'a': 'alfa',
	'b': 'bravo',
	'c': 'charlie',
	'd': 'delta',
	'e': 'echo',
	'f': 'foxtrot',
	'g': 'golf',
	'h': 'hotel',
	'i': 'india',
	'j': 'juliett',
	'k': 'kilo',
	'l': 'lima',
	'm': 'mike',
	'n': 'november',
	'o': 'oscar',
	'p': 'papa',
	'q': 'quebec',
	'r': 'romeo',
	's': 'sierra',
	't': 'tango',
	'u': 'uniform',
	'v': 'victor',
	'w': 'whiskey',
	'x': 'x-ray',
	'y': 'yankee',
	'z': 'zulu'
}
name = input('What is your name? ').lower()
for letter in name:
	for key, value in d.items():
		if letter == key:
			print(value.capitalize())

# Transponovana matice
a = [[1,2,3], [4,5,6], [7,8,9]]
b = []
for m in a:
	c = []
	for num in m:
		c.append(num)
	b.append(c)
print(b)

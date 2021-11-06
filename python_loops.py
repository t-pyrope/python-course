# 1. Seznamy
name_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef', 'Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal', 'Lenka', 'Katerina']
user_name = input('Your name? ')
if user_name in name_list:
	print('Hello {0}'.format(user_name))
else:
	print("Sorry, we don't know such a name. Are you Czech at all?")

# 2. Smycky
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

# 3. Transponovana matice
a = [[1,2,3], [4,5,6], [7,8,9]]
b = []
for m in a:
	c = []
	for num in m:
		c.append(num)
	b.append(c)
print(b)

# 4. Nakupni seznam
shopping_list = ['eggs', 'milk', 'bacon']
item_to_buy = input('What do you want to buy? ').lower()
for item in shopping_list:
	if item == item_to_buy:
		print('You already have this item')
		print(item_to_buy)
		break
shopping_list.append(item_to_buy)
shopping_list = list(set(shopping_list))

# 5. List comprehension
nums = [1,2,3,4,5]
favorites = ['{0} is my favorite number!'.format(str(x**2)) for x in nums]
print(nums)
print(favorites)

# 6. GATTACA
string = input('Enter string ')
string_list = list(string)
pos = [i for i, letter in enumerate(string_list) if letter == 'A']
if len(pos) > 0:
	print("'A' occurs in the word {0} in this positions: {1}".format(string, str(pos)))
else:
	print("There is no 'A's in the word {0}".format(string))

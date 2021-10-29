# 1. Dedictvi
1256983 % 28

# 2. Overeni matematickych vysledku
(12**52)%15 < 8 or 3**5 > 100
5*(3**3) != 900/75
not (5*(3**3) == 900/75)

# 3. Baleni do zavorek nebo mnozeni pismen
'[[]]'[0:2:] + 'PYTHON' + '[[]]'[2::]
'Python'[-2::] * 4
'Perl'[2] * 6

# 4. Hratky s retezci
def make_half_upper(str):
	return str[0:len(str)//2:].upper() + str[len(str)//2::].lower()
half_upper('Python')

def create_string(str):
	return str[0] * len(str)
create_string('python')
create_string('git')

# 5. Vyreseni chyby
print(7 + 3 * 2) # 13
print('7' + str(3*2) ) # 76
print('7' + '3*2') # 73*2
# print('7' + 3*2) # we cannot concatenate string with variable of another type

# 6. Hobby promenna
hobby = 'reading'
print('My hobby is {0}'.format(hobby))

date = '2018-11-01'
print('{0}/{1}'.format(date[-2::], date[-5:-3:]))

# 7. Prace se seznamy
hobbies =[]
hobbies.append('reading')
hobbies.append('drinking coffee')
hobbies.append('procrastinating')
hobbies.append('listening to music')
print('My hobby that I like most is {0}'.format(hobbies[1]))
print('My hobby that I like least is {0}'.format(hobbies[2]))
del hobbies[2]

# 8. Razeni mest
cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
cities.sort()
"*".join(cities)

# 9. Zen of Python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
zen = """
Beautiful is better that ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuce the temptation of guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better that never.
Althought never is oftern better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementaion is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
alphabet_set = set(alphabet)
zen_set = set(zen.lower())
zen_set.remove('-')
zen_set.remove(',')
zen_set.remove('.')
zen_set.remove('*')
zen_set.remove('\n')
zen_set.remove('!')
zen_set.remove("'")
zen_set.remove(' ')

print('These letters are not in zen of Python: {0}'.format(alphabet_set.difference(zen_set)))

# 10. Odstraneni ze slovniku
d = {'payton': 'An interpreted, object-oriented programming language'}
d['Python'] = d['payton']
del d['payton']

alex_turner = ('Alex', 'Turner')
hannah_murray = ('Hannah', 'Murray')
phone_book = {alex_turner: '+123456789'}
phone_book[hannah_murray] = '+987654321'

# 11. Prace se slovnikem
info = {('Name', 'Surname'):('John', 'Doe')}
john_doe = info[('Name', 'Surname')]
print('{0}_{1}'.format(john_doe[0], john_doe[1]))

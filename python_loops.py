# 1. seznamy
name_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef', 'Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal', 'Lenka', 'Katerina']
user_name = input('Your name? ')
if user_name in name_list:
	print('Hello {0}'.format(user_name))
else:
	print("Sorry, we don't know such a name. Are you Czech at all?")

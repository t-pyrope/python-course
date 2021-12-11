import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'things_list.txt')

things_list = ["casserole", "book", "knife", "water bottle", "fishing rod"]

with open(filename, 'w', encoding="utf-8") as f:
	for i, thing in enumerate(things_list):
		if (i < (len(things_list) - 1)):
			f.write(str(i+1) + ' ' + thing + '\n')
		else:
			f.write(str(i+1) + ' ' + thing)

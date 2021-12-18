import argparse

parser = argparse.ArgumentParser()

parser.add_argument('string', help="a string which letters are counted")

parser.add_argument("-v", "--vowels", help="count only vowels", action="store_true")

parser.add_argument("-c", "--consonants", help="count only consonants", action="store_true")

args = parser.parse_args()

if args.vowels and not args.consonants:
	vowels_list = ["a", "e", "i", "o", "u", "y"]
	vowels = {v: 0 for v in vowels_list}
	for letter in args.string:
		string = str(letter).lower()
		if string in vowels.keys():
			vowels[string] = vowels[string] + 1
	print("Calculated vowels:")
	for key, value in vowels.items():
		if value > 0:
			print(key, value)
elif args.consonants and not args.vowels:
	consonants_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
	consonants = {c: 0 for c in consonants_list}
	for letter in args.string:
		string = str(letter).lower()
		if string in consonants.keys():
			consonants[string] = consonants[string] + 1
	print("Calculated consonants:")
	for key, value in consonants.items():
		if value > 0:
			print(key, value)
else:
	letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	letters = {l: 0 for l in letters_list}
	for letter in args.string:
		string = str(letter).lower()
		if string in letters.keys():
				letters[string] = letters[string] + 1
	print("Calculated letters:")
	for key, value in letters.items():
		if value > 0:
			print(key, value)

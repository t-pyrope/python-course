import argparse

parser = argparse.ArgumentParser()

parser.add_argument('string', help="a string which letters are counted")

parser.add_argument("-v", "--vowels", help="count only vowels", action="store_true")

parser.add_argument("-c", "--consonants", help="count only consonants", action="store_true")

args = parser.parse_args()

if args.vowels and not args.consonants:
	vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "y": 0}
	for letter in args.string:
		string = str(letter).lower()
		if string in vowels.keys():
			vowels[string] = vowels[string] + 1
	print("Calculated vowels:")
	for key, value in vowels.items():
		if value > 0:
			print(key, value)
elif args.consonants and not args.vowels:
	consonants = {"b": 0, "c": 0, "d": 0, "f": 0, "g": 0, "h": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "v": 0, "w": 0, "x": 0, "z": 0}
	for letter in args.string:
		string = str(letter).lower()
		if string in consonants.keys():
			consonants[string] = consonants[string] + 1
	print("Calculated consonants:")
	for key, value in consonants.items():
		if value > 0:
			print(key, value)
else:
	letters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
	for letter in args.string:
		string = str(letter).lower()
		if string in letters.keys():
				letters[string] = letters[string] + 1
	print("Calculated letters:")
	for key, value in letters.items():
		if value > 0:
			print(key, value)

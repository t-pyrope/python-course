import argparse

parser = argparse.ArgumentParser()

parser.add_argument('word', help="a word where the specified letter is going to be deleted")

parser.add_argument('letter', help="a letter which is going to be deleted from the given word")

args = parser.parse_args()

word_list = list(str(args.word));
letter = str(args.letter)

for i, el in enumerate(word_list):
	if el == letter:
		del word_list[i]

print("".join(word_list))

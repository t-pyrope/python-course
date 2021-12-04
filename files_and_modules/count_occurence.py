import argparse

parser = argparse.ArgumentParser()

parser.add_argument('substring', help="a substring for search in main string")

parser.add_argument('string', help="a string, where the number of occurence of substring is calculated")

args = parser.parse_args()

substring = str(args.substring)
string = str(args.string)
occurence_num = 0
pos = 0

while True:
	foundPos = string.find(substring, pos)
	if foundPos == -1:
		break;
	occurence_num += 1
	pos = foundPos + 1

print("String", substring, "occured", occurence_num, "times in string", string)

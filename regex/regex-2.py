import os
import re

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'zen.txt')
with open(filename, 'r', encoding='utf-8') as f:
	zen_lines_list = f.read().splitlines();

a_o_before_dot = 0
alphanumeric = 0
t_two_times = 0
t_one_or_two_times = 0


for i, line in enumerate(zen_lines_list):
	match_a_o_before_dot = re.search(r'(a|o)\.', line)
	match_t_two_times = re.search(r'(t|T){2}', line)
	match_t_one_or_two_times = re.search(r'(t|T){1,2}', line)
	if match_a_o_before_dot :
		a_o_before_dot += 1

	for letter in line:
		match_alphanumeric = re.search(r'[a-zA-Z0-9]', letter)
		if match_alphanumeric:
			alphanumeric += 1

	for word in line.split(' '):
		match_t_two_times = re.search(r'(t|T){2}', word)
		match_t_one_or_two_times = re.search(r'(t|T){1,2}', word)
		if match_t_two_times:
			t_two_times += 1
		if match_t_one_or_two_times:
			t_one_or_two_times += 1

print("Found in zen:")
print(a_o_before_dot, "lines where there is letter a or o before dot")
print(alphanumeric, "alphanumeric symbols")
print(t_two_times, "words, where T letter (uppercase and lowercase) is repeated two times")
print(t_one_or_two_times, "words, where T letter (uppercase and lowercase) is repeated 1 to 2 times")

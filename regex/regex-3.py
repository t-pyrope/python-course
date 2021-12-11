import re

def get_name():
	while True:
		name = input("Enter your name ")
		match_letters = re.match(r'^[a-zA-Z]*$', name)
		match_capitalized = re.match(r'^[A-Z]+.*$', name)
		if match_letters and match_capitalized:
			print("We have got your name:", name)
			break
		elif match_letters and not match_capitalized:
			print("The name should start with an uppercase letter")
		elif match_capitalized  and not match_letters:
			print("The name should contain only letters")
		else:
			print("The name should start with and uppercase and contain only letters")

get_name()

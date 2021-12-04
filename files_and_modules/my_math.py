def divide_two_numbers(a,b):
	try:
		division = a // b
	except ZeroDivisionError:
		print("Division by zero")
	except TypeError:
		print("Didn't get integers")
	else:
		print(division)
		return
	print('Quit calculation')
	return

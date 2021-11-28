# 1.1 Prvni cviceni na zaklady funkci
def divide(dividend, divisor):
	if divisor == 0:
		return 'You cannot divide by zero'
	return dividend // divisor
divide(1, 0)
divide(2, 1)

# 1.2 Druhe cviceni na zaklady funkci
def sum_nums(num_list):
	list_sum = 0
	for num in num_list:
		list_sum += num
	print('The sum is', list_sum)
sum_nums([1,2,3])

# 2. Lambda funkce
compare_list = lambda num_list: print('big list') if len(num_list) > 5 else print('small list')
compare_list([1,2,3,4])

# 3. Funkce s jednim parametrem
def string_upper_lower(s):
	upper_count = 0
	lower_count = 0
	for letter in s:
		if letter.isupper():
			upper_count += 1
		elif letter.islower():
			lower_count += 1
	print('String:', s)
	print('Uppercase letters:', upper_count)
	print('Lowercase letters:', lower_count)
string_upper_lower('Peter Piper picked')

# 4. Funkce s dvema parametry
def meal_vouchers(lunch_cost, voucher_value):
	cash = lunch_cost % voucher_value
	voucher_pcs = lunch_cost // voucher_value
	print('Lunch cost:', lunch_cost, 'CZK')
	print('Pay in cash:', cash, 'CZK')
	print('Pay in meal vouchers:', voucher_pcs, 'pcs,', voucher_value, 'CZK each')
meal_vouchers(500, 74)

# 5. Rekurzivni funkce
def compute_factorial(num):
	if num < 0:
		return 'num is not a positive integer'
	if num == 0:
		return 1
	if num != 0:
		num *= compute_factorial(num - 1)
	return num
print(compute_factorial(5))

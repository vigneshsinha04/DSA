def FactorialRecursive(number):
	if number == 2:
		return 2
	return number* FactorialRecursive(number-1)

def FactorialIterative(number):
	ans = 1
	for i in range(1,number+1):
		ans = ans*i
	return ans

def FactorialWhile(number):
	ans = 1
	while number:
		ans = ans*number
		number = number-1
	return ans
		
print(FactorialRecursive(7))
print(FactorialIterative(5))
print(FactorialWhile(7))
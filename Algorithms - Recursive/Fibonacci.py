def FibonacciRecursive(number): #Big-O = 2^n Exponential
	if number < 2:
		return number
	return FibonacciRecursive(number-1) + FibonacciRecursive(number-2)

def FibonacciIterative(number):
	num1 = 0
	num2 = 1
	num3 = 0
	for i in range(0,number-1):
		num3 = num1 + num2
		num1 = num2
		num2 = num3
	return num3

print(FibonacciRecursive(5))
print(FibonacciIterative(5))

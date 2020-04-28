def fibonacciMemoization(fibonacci):
	cache = {}
	def wrapper(n):
		if n not in cache:
			cache[n] = fibonacci(n)
		return cache[n]
	return wrapper

@fibonacciMemoization
def fibonacci(n):
	print('Long Tme')
	if n < 2:
		return n
	return fibonacci(n-1) + fibonacci(n-2)



print(fibonacci(5))
print(fibonacci(6))

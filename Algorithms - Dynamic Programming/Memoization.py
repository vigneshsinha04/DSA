# Using Decorators

def memoizeDecorator(addToEighty):
	cache = {}
	def wrapper(n):
		if n not in cache:
			cache[n] = addToEighty(n)
		return cache[n]
	return wrapper

@memoizeDecorator
def addToEighty(n):
	print('Long Time')
	return n+80

print(addToEighty(6))
print(addToEighty(6))
print(addToEighty(5))
print(addToEighty(5))
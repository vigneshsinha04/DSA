def reverse(string):
	if type(string) != str:
		return 'Please Enter a string!'
	li = []
	for i in range(len(string)-1, -1, -1):
		li.append(string[i])
	return ''.join(li)

print(reverse('Hi!!! I am Hector'))
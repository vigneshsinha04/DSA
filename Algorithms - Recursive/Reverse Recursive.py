def reverseString(string):
  if string == '':
    return ''
  return reverseString(string[1:]) + string[0]

print(reverseString('Hector'))
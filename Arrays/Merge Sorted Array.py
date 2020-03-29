def MergeSortedArray(array1, array2):
	if len(array1)==0 or len(array2)==0:
		return a+b

	a,b=0,0
	li=[]

	while a<len(array1) and b<len(array2):

		if array1[a] <= array2[b]:
			li.append(array1[a])
			a+=1

		elif array2[b] < array1[a]:
			li.append(array2[b])
			b+=1

	li += array1[a:] + array2[b:]
	return li

print(MergeSortedArray([1,2,5], [2,4,6,9,14]))
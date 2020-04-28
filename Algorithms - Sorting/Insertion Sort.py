def InsertionSort(array):
	length = len(array)
	i=1
	end = array[0]
	while i < length:
		if array[i] < end:
			x = array.pop(i)
			for j in range(0,i):
				if x < array[j]:
					array.insert(j,x)
					break
		end = array[i]
		i+=1
	return array	

arr= [5,8,1,89,75,12,36,2,75,49]
print(InsertionSort(arr))
print(sorted(arr))
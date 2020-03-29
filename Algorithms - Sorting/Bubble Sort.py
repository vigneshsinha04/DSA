def BubbleSort(array):
	arr_len = 0
	if arr == []:
		return arr
	while arr_len < len(arr):
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
		arr_len +=1
	return arr

arr = [5,8,1,89,75,12,36,2,75,49]
print(BubbleSort(arr))
print(sorted(arr))
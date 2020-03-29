def SelectionSort(array):
	if array == '':
		return array
	for i in range(len(array)):
		min = array[i]
		for j in range(i+1, len(array)):
			if array[j] < array[i]:
				min = array[j]
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
	return arr

# def selectionsort(arr):
#   i = 0
#   while i < len(arr):
#     min = arr[i]
#     index = i
#     for j in range(i+1,len(arr)):
#       if arr[j] < min:
#         index = j
#         min = arr[j]
#     arr[i] , arr[index] = arr[index] , arr[i]
#     i += 1
  
#   return arr

arr= [5,8,1,89,75,12,36,2,75,49]
print(SelectionSort(arr))
print(sorted(arr))

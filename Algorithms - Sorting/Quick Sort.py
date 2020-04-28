def partition(array,low,high):
    i = low
    pivot = array[high]

    for j in range(low,high):
        if array[j] < pivot:
            array[i],array[j] = array[j],array[i]
            i+=1
    array[i],array[high] = array[high],array[i]
    return i

def quickSort(array, low, high):
    if low < high:
        pi = partition(array,low,high)

        quickSort(array,low,pi-1)
        quickSort(array,pi+1, high)

# arr = [99,44,6,2,1,5,63,87,283,4,0]
arr = ['k','g','r','f','Q','A','a','z','c']
n = len(arr)-1
quickSort(arr,0,n)
print(arr)
print(sorted(arr))



# def partition(arr,low,high): 
#     i = low
#     pivot = arr[high]
  
#     for j in range(low , high):
#         if   arr[j] <= pivot:              
#             arr[i],arr[j] = arr[j],arr[i] 
#             i += 1  
#     arr[i],arr[high] = arr[high],arr[i] 
#     return (i)

# def quickSort(arr,low,high): 
#     if low < high:
#         pi = partition(arr,low,high)

#         quickSort(arr, low, pi-1) 
#         quickSort(arr, pi+1, high)


# arr = [10, 7, 8, 9, 1, 5] 
# n = len(arr) 
# quickSort(arr,0,n-1) 
# print(arr)
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = (l + r)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid+1

        elif arr[mid] > x:
            r = mid-1
    return -1  

arr = [ 2, 3, 4, 10, 40 ]
x = 40
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}")
else: 
    print("Element is not present in array")
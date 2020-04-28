def MergeSort(array):
  if len(array) == 1:
    return array
  length = len(array)
  mid = length//2
  left = array[:mid]
  right = array[mid:]

  return merge(MergeSort(left), MergeSort(right))

def merge(left, right):
  result = []
  leftIndex = 0
  rightIndex = 0

  while leftIndex < len(left) and rightIndex < len(right):
    if left[leftIndex] < right[rightIndex]:
      result.append(left[leftIndex])
      leftIndex +=1
    else:
      result.append(right[rightIndex])
      rightIndex +=1

  return result + left[leftIndex:] + right[rightIndex:]


arr = [99,44,6,2,1,5,63,87,283,4,0]
print(MergeSort(arr))
print(sorted(arr))

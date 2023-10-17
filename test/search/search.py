def linear_search(arr, target):
  for index, value in enumerate(arr):
    if target == value:
      return index
  return -1

def binary_search(arr, target):
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1 



arr = [1, 3, 5, 2, 4, 6, 8, 7, 9, 10]
# index = linear_search(arr, 1)
# print(index)
arr = sorted(arr)
print(arr)
index = binary_search(arr, 20)
print(index)
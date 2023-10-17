# unordered list
arr = [1, 3, 5, 2, 4, 6, 8, 7, 9, 10]

for i in range(len(arr)):
  for j in range(len(arr) - i - 1):
    if arr[j] > arr[j + 1]:
      arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
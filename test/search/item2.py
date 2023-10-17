def search_num(arr,target):
  for idx, val in enumerate(arr):
    if val > target:
      return idx
  return -1

arr, target = input('Enter Input : ').split('/')
arr = sorted(list(map(int, arr.split())))
target = list(map(int, target.split()))

for i in target:
  idx = search_num(arr, i)
  if idx == -1:
    print('Not Found')
  else:
    print(f'Value = {arr[idx]}')
n = int(input('Enter Input : '))

length = n * 2 + 4

mid = length // 2

for i in range(mid):
  for j in range(length):
    if j >= mid:
      if i != mid - 1 and i != 0 and j != mid and j != length - 1:
        print('#', end='')
      else:
        print('+', end='')
    else:
      if j < mid - (i + 1):
        print('.', end='')
      else:
        print('#', end='')
  print()

for i in range(mid, 0, -1):
  for j in range(length):
    if j >= mid:
      if j < length - (mid - i):
        print('+', end='')
      else:
        print('.', end='')
    else:
      if i != mid and i != 1 and j != 0 and j != mid - 1:
        print('+', end='')
      else:
        print('#', end='')
  print()

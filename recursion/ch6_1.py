a = []
b = []
c = []


def display(maxn, row):
  rev_a = a[::-1]
  rev_b = b[::-1]
  rev_c = c[::-1]
  if row == 0:
    return
  if row == maxn:
    print('|  |  |')
  if len(a) >= row:
    print(f"{rev_a[row-1]}  ", end="")
  else:
    print('|  ', end="")
  if len(b) >= row:
    print(f"{rev_b[row-1]}  ", end="")
  else:
    print('|  ', end="")
  if len(c) >= row:
    print(f"{rev_c[row-1]}", end="")
  else:
    print('|', end="")
  if row != 0:
    print()
  display(maxn, row-1)


def pop_insert(start, end):
  if start == 'A':
    x = a.pop(0)
  elif start == 'B':
    x = b.pop(0)
  elif start == 'C':
    x = c.pop(0)
  if end == 'A':
    a.insert(0, x)
  elif end == 'B':
    b.insert(0, x)
  elif end == 'C':
    c.insert(0, x)


def move(n, A, B, C, maxn):
  if n == 1:
    print(f"move {n} from  {A} to {C}")
    pop_insert(A, C)
    display(maxn, maxn)
  else:
    move(n-1, A, C, B, maxn)
    print(f"move {n} from  {A} to {C}")
    pop_insert(A, C)
    display(maxn, maxn)
    move(n-1, B, A, C, maxn)


def init(i, target):
  global a
  if i <= target:
    a.append(i)
    init(i+1, target)


if __name__ == '__main__':
  n = int(input("Enter Input : "))
  init(1, n)
  display(n, n)
  move(n, 'A', 'B', 'C', n)

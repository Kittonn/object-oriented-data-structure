def perket(inputs, s, b, n, min):
  if n < 0:
    return min

  s *= inputs[n][0]
  b += inputs[n][1]

  if abs(s - b) < min:
    min = abs(s - b)

  return perket(inputs, s, b, n - 1, min)


if __name__ == "__main__":
  inputs = [[int(i) for i in i.split()]
            for i in input("Enter Input : ").split(',')]
  m = perket(inputs, 1, 0, len(inputs) - 1, 1000000001)
  print(m)

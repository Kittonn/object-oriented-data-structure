def perket(s=1, b=0, n=0):
  if n >= len(inputs):
    return
  else:
    s *= inputs[n][0]
    b += inputs[n][1]
    
    result = abs(s - b)
    
    global m
    m = min(result, m)

    perket(s, b, n + 1)


if __name__ == "__main__":
  inputs = [[int(i) for i in i.split()]
            for i in input("Enter Input : ").split(',')]
  m = int(10e9)

  perket(1, 0, len(inputs) - 1)
  print(m)

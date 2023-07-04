print('*** multiplication or sum ***')

n, m = [int(i) for i in input('Enter num1 num2 : ').split()]

product = n*m

if (product <= 1000):
  print(f'The result is {product}')
elif (product > 1000):
  print(f'The result is {n+m}')

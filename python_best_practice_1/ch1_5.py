class MyInt:
  def __init__(self, num) -> None:
    self.num = num
  
  def isPrime(self):
    flag= False
    if self.num <= 1:
        return False
    elif self.num > 1:
        for i in range(2, self.num):
            if (self.num % i) == 0:
                flag = True
                break
            
        if flag:
          return False
        else:
          return True
  def showPrime(self):
    nums = []
    for num in range(2, self.num + 1):
      if num > 1:
          for i in range(2, num):
              if (num % i) == 0:
                  break
          else: 
              nums.append(num)
    return nums

  def __sub__(self, other):
    return int(self.num - (other.num // 2))

print(' *** class MyInt ***')

n1, n2 = [int(e) for e in input('Enter 2 number : ').split()]

num1 = MyInt(n1)
num2 = MyInt(n2)

print('{} isPrime : {}'.format(num1.num, num1.isPrime()))
print('{} isPrime : {}'.format(num2.num, num2.isPrime()))
print('Prime number between 2 and {} : '.format(num1.num), end='')

if (num1.num < 2):
  print('!!!A prime number is a natural number greater than 1')
else:
  print(*num1.showPrime(), sep=' ')
print('Prime number between 2 and {} : '.format(num2.num), end='')
if (num2.num < 2):
  print('!!!A prime number is a natural number greater than 1')
else: 
  print(*num2.showPrime(), sep=' ')
print('{} - {} = {}'.format(num1.num, num2.num, num1 - num2))
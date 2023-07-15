class Stack:
  def __init__(self):
    self.stack = []

  def pop(self):
    return self.stack.pop() if not self.is_empty() else None

  def push(self, value):
    return self.stack.append(value)

  def peek(self):
    return self.stack[-1] if not self.is_empty() else None

  def is_empty(self):
    return self.stack == []

  def size(self):
    return len(self.stack)
  
def soi_ton(max_car, cars, command, car):
  stack = Stack()
  
  for i in cars:
    if i != '0':
      stack.push(int(i)) 
    
  if command == 'arrive':
    if stack.size() < max_car and car not in stack.stack:
      stack.push(car)
      print(f'car {car} arrive! : Add Car {car}')
    elif car in stack.stack:
      print(f'car {car} already in soi')
    else:
      print(f'car {car} cannot arrive : Soi Full')
  
  elif command == 'depart':
    if stack.is_empty():
      print(f'car {car} cannot depart : Soi Empty')
    elif car in stack.stack:
      stack.stack.remove(car)
      print(f'car {car} depart ! : Car {car} was remove')
    elif car not in stack.stack:
      print(f'car {car} cannot depart : Dont Have Car {car}')
      
    
  print(stack.stack)
  
if __name__ == '__main__':
  print('******** Parking Lot ********')
  
  max_car, cars, command, car = [i for i in input("Enter max of car,car in soi,operation : ").split()]
  
  soi_ton(int(max_car), cars.split(','), command, int(car))
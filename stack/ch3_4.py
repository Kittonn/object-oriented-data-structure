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
  
def into_the_woods(n):
  stack = Stack()
  for i in n:
    if i[0] == 'A':
      while not stack.is_empty() and stack.peek() < int(i[1]):
        stack.pop()
      if stack.peek() != int(i[1]):
        stack.push(int(i[1]))
    elif i[0] == 'B':
      print(stack.size())

if __name__ == '__main__':
  n = [i.split() for i in input("Enter Input : ").split(",")]
  
  into_the_woods(n)
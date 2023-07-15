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

def precedence(operator):
  return {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}.get(operator, 0)

def infix_2_postfix(infix):
  stack = Stack()
  postfix = []

  for i in infix:
    if i.isalpha():
      postfix.append(i)
    elif i == '(':
      stack.push(i)
    elif i == ')':
      while not stack.is_empty() and stack.peek() != '(':
        postfix.append(stack.pop())
      stack.pop()
    else:
      while not stack.is_empty() and precedence(stack.peek()) >= precedence(i):
        postfix.append(stack.pop())
      stack.push(i)
  
  while not stack.is_empty():
    postfix.append(stack.pop())
  
  return ''.join(postfix)


if __name__ == '__main__':
  infix = input('Enter Infix : ')
  postfix = infix_2_postfix(infix)
  print(f'Postfix : {postfix}')

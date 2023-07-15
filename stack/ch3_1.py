class Stack:
  def __init__(self):
    self.stack = []

  def __str__(self):
    if self.size() == 0:
      return f"{self.size()}\nPerfect ! ! !"
    else:
      return f"{self.size()}"

  def pop(self):
    return self.stack.pop() if not self.is_empty() else None

  def push(self, item):
    return self.stack.append(item)

  def peek(self):
    return self.stack[-1] if not self.is_empty() else None

  def is_empty(self):
    return self.stack == []

  def size(self):
    return len(self.stack)


def parentheses_matching(parentheses):
  stack = Stack()
  opening = ['(', '[']
  closing = [')', ']']

  for i in parentheses:
    if i in opening:
      stack.push(i)
    elif i in closing:
      if not stack.is_empty() and stack.peek() == opening[closing.index(i)]:
        stack.pop()
      else:
        stack.push(i)

  print(stack)


if __name__ == "__main__":
  parentheses_matching(input('Enter Input : '))

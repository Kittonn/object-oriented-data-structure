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
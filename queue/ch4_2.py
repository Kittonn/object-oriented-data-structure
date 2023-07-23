class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    return self.queue.pop(0)

  def is_empty(self):
    return self.queue == []

  def size(self):
    return len(self.queue)
  
if __name__ == '__main__':
  word, time = input('Enter people and time : ').split()
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


def basic_queue(commands):
  queue = Queue()

  for command in commands:
    if command[0] == 'E':
      queue.enqueue(command[1])
      print(f'Add {command[1]} index is {queue.size()-1}')
    else:
      if not queue.is_empty():
        deleted_item = queue.dequeue()
        print(f'Pop {deleted_item} size in queue is {queue.size()}')
      else:
        print(-1)

  if queue.is_empty():
    print('Empty')
  else:
    print(f'Number in Queue is :  {queue.queue}')


if __name__ == '__main__':
  commands = [command.split() for command in input('Enter Input : ').split(",")]

  basic_queue(commands)

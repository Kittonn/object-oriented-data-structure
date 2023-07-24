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


def search_portal(width, height, room):
  if 'F' not in room or len(room) != width * height:
    print("Invalid map input.")
    

if __name__ == '__main__':
  width, height, room = input('Enter width, height, and room: ').split()
  
  search_portal(int(width), int(height), room)

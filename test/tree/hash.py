class Data:
  def __init__(self, key, value):
    self.key = key
    self.value = value

class HashTable:
  def __init__(self, table_size, max_collision):
    self.table_size = table_size
    self.max_collision = max_collision
    self.size = 0
    self.table = [None] * table_size

  def insert(self, data):
    if self.size == self.table_size:
      print("This table is full")
      exit(0)

    hash_index = sum([ord(ch) for ch in data.key]) % self.table_size
    for i in range(self.max_collision):
      index = (hash_index + pow(i, 2)) % self.table_size
      if self.table[index] is None:
        self.table[index] = data
        self.size += 1
        return
      

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.count_path = []

  def insert(self, data):
    self.root = self._insert(self.root, data)

  def _insert(self, node, data):
    if node is None:
      return Node(data)
    if data < node.data:
      node.left = self._insert(node.left, data)
    elif data >= node.data:
      node.right = self._insert(node.right, data)
    return node

  def print_breadth(self):
    queue = [self.root]
    while len(queue) > 0:
      node = queue.pop(0)
      print(node.data, end=' ')
      if node.left is not None:
        queue.append(node.left)
      if node.right is not None:
        queue.append(node.right)

  def find_count_path(self):
    self._find_count_path(self.root, 0)
    return self.count_path[::-1]

  def _find_count_path(self, node, count):
    if node is None:
      return
    
    if node.left is None and node.right is None:
      self.count_path.append(count)
      return
    
    self._find_count_path(node.left, count + 1)
    self._find_count_path(node.right, count + 1)


def find_num_and_count(arr):
  num = {}
  for i in arr:
    if i not in num:
      num[i] = 1
    else:
      num[i] += 1
  return num


if __name__ == '__main__':
  inputs = input('Enter input: ').split()
  tree = BinarySearchTree()

  for item in inputs:
    tree.insert(int(item))

  count_path = tree.find_count_path()
  print(f'{len(count_path)} path(s)')
  num = find_num_and_count(count_path)
  new_num = sorted(num.items(),reverse=True)
  
  for key,item in new_num:
    print(f'{item} path(s) that pass through {key} node(s)')
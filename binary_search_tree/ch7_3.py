class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    self.root = self._insert(self.root, data)

  def _insert(self, node, data):
    if node is None:
      return Node(data)
    if data < node.data:
      node.left = self._insert(node.left, data)
    elif data > node.data:
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
  
  def find_maximum_path(self):
    return self._find_maximum_path(self.root)

  def _find_maximum_path(self, node):
    if node is None:
      return []
    
    left = self._find_maximum_path(node.left)
    right = self._find_maximum_path(node.right)

    if sum(left) > sum(right):
      return [node.data] + left
    else:
      return [node.data] + right
    
    
    
if __name__ == '__main__':
  inputs = input('Enter tree: ').split()
  tree = BinarySearchTree()

  for item in inputs:
    tree.insert(int(item))

  print("Breadth : ", end='')
  tree.print_breadth()
  print()

  print(tree.find_maximum_path())

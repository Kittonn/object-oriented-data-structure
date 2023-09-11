class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class ExpressionTree:
  def __init__(self):
    self.root = None

  def build_tree(self, postfix):
    stack = []
    operations = ['+', '-', '*', '/']

    for i in postfix:
      new_node = Node(i)
      if i not in operations:
        stack.append(new_node)
      else:
        new_node.right = stack.pop()
        new_node.left = stack.pop()
        stack.append(new_node)
  
    if stack:
      self.root = stack.pop()

  def print_inorder(self):
    self._print_inorder(self.root)

  def _print_inorder(self, node):
    if node is None:
      return
    
    if node.data in ['+', '-', '*', '/']:
      print('(', end='')
    self._print_inorder(node.left)
    print(node.data, end='')
    self._print_inorder(node.right)
    if node.data in ['+', '-', '*', '/']:
      print(')', end='')
  
  def print_preorder(self):
    self._print_preorder(self.root)

  def _print_preorder(self, node):
    if node is None:
      return
    
    print(node.data, end='')
    self._print_preorder(node.left)
    self._print_preorder(node.right)
    
  def show_tree(self):
    self._show_tree(self.root, 0)

  def _show_tree(self, node, level):
    if node is None:
      return
  
    self._show_tree(node.right, level + 1)
    print(' ' * 5 * level, node.data)
    self._show_tree(node.left, level + 1)


if __name__ == '__main__':
  inputs = input('Enter Postfix : ')
  tree = ExpressionTree()
  tree.build_tree(inputs)
  print('Tree :')
  tree.show_tree()
  print('--------------------------------------------------')
  print('Infix : ', end='')
  tree.print_inorder()
  print()
  print('Prefix : ', end='')
  tree.print_preorder()
  print()
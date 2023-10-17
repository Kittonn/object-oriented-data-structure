class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data >= node.data:
            node.right = self._insert(node.right, data)
        node = self._balance(node)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return node
    
    def _balance(self, node):
        balance = self._get_balance(node)
        
        if balance == -2:
            if self._get_balance(node.right) == 1:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        elif balance == 2:
            if self._get_balance(node.left) == -1:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        return node
    
    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(
            self._get_height(new_root.left), self._get_height(new_root.right)
        )
        return new_root
    
    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(
            self._get_height(new_root.left), self._get_height(new_root.right)
        )
        return new_root

    def _get_height(self, node):
        return node.height if node else 0
        
    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)
    
    def print_tree(self, node, level=0):
        if node is None:
            return
        
        self.print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.data)
        self.print_tree(node.left, level + 1)

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 25]

    avl = AVL()

    for i in arr:
        avl.insert(i)

    avl.print_tree(avl.root)
    

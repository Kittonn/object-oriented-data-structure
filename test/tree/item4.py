class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BST:
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
        return node

    def print_inorder(self):
        self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node is None:
            return

        self._print_inorder(node.left)
        print(node.data, end=" ")
        self._print_inorder(node.right)

    def print_preorder(self):
        self._print_preorder(self.root)

    def _print_preorder(self, node):
        if node is None:
            return

        print(node.data, end=" ")
        self._print_preorder(node.left)
        self._print_preorder(node.right)

    def print_postorder(self):
        self._print_postorder(self.root)

    def _print_postorder(self, node):
        if node is None:
            return

        self._print_postorder(node.left)
        self._print_postorder(node.right)
        print(node.data, end=" ")

    def print_breadth(self):
        queue = [self.root]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def delete_node(self, data):
        self.root = self._delete_node(self.root, data)

    def _delete_node(self, node, data):
        if node is None:
            return

        if data < node.data:
            node.left = self._delete_node(node.left, data)
        elif data > node.data:
            node.right = self._delete_node(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.data = self._find_min(node.right)
                node.right = self._delete_node(node.right, node.data)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node.data

if __name__ == "__main__":
    inputs = input("Enter Input : ").split()
    tree = BST()

    for item in inputs:
        tree.insert(int(item))

    print("Preorder : ", end="")
    tree.print_preorder()
    print()
    print("Inorder : ", end="")
    tree.print_inorder()
    print()
    print("Postorder : ", end="")
    tree.print_postorder()
    print()
    print("Breadth : ", end="")
    tree.print_breadth()
    print()

    print("Delete : ", end="")
    tree.delete_node(int(input()))

    print("Preorder : ", end="")
    tree.print_preorder()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                elif data >= current.data:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
        return self.root
        

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

    def descending(self, node):
        if node is None:
            return
        if node.right is not None:
            self.descending(node.right)
        print(node.data, end=" ")
        if node.left is not None:
            self.descending(node.left)


    def ascending(self, node):
        if node is None:
            return
        if node.left is not None:
            self.ascending(node.left)
        print(node.data, end=" ")
        if node.right is not None:
            self.ascending(node.right)


T = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Descending: ", end="")
T.descending(root)
print()
print("Ascending: ", end="")
T.ascending(root)
print()
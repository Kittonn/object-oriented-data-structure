class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
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

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print("     " * level, node.data)
            self.printTree(node.left, level + 1)

    def find_node(self, data):
        return self._find_node(self.root, data)

    def _find_node(self, node, data):
        if node is None:
            return None

        if node.data == data:
            return node

        if data < node.data:
            return self._find_node(node.left, data)
        else:
            return self._find_node(node.right, data)

    def burn(self, data):
        target = self.find_node(data)
        if target is None:
            print(f"There is no {data} in the tree.")
            return

        will_burn = [target]
        burned = [target]

        while will_burn:
            for node in will_burn:
                burned.append(node)
                print(node.data, end=" ")
            will_burn = self._burn(will_burn, burned)
            print()

    def _burn(self, will_burn, burned):
        new_will_burn = []
        for node in will_burn:
            if node.left and node.left not in burned:
                new_will_burn.append(node.left)
            if node.right and node.right not in burned:
                new_will_burn.append(node.right)
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if (
                node.left in will_burn or node.right in will_burn
            ) and node not in burned:
                new_will_burn.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return new_will_burn


if __name__ == "__main__":
    arr, burn = input("Enter node and burn node : ").split("/")
    arr = list(map(int, arr.split()))
    burn = int(burn)

    tree = AVL()

    for item in arr:
        tree.insert(item)

    tree.burn(burn)

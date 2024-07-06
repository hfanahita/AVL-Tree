class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    @staticmethod
    def get_height(node):
        if node is None:
            return 0
        return node.height
    def update_height(self):
        self.height = 1 + max(Node.get_height(self.left), Node.get_height(self.right))
    def get_balance(self):
        return Node.get_height(self.left) - Node.get_height(self.right)
from Node import *


class AVLTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def rotate_right(node):
        if node is None:
            return node
        tmp = node.left
        node.left = tmp.right
        tmp.right = node

        node.update_height()
        tmp.update_height()
        return tmp

    @staticmethod
    def rotate_left(node):
        if node is None:
            return node
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        node.update_height()
        tmp.update_height()
        return tmp

    @staticmethod
    def __insert(node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = AVLTree.__insert(node.left, key)
        elif key > node.key:
            node.right = AVLTree.__insert(node.right, key)
        else:
            return node
        node.update_height()
        balance = node.get_balance()
        if balance > 1:
            if key < node.left.key:
                return AVLTree.rotate_right(node)
            else:
                node.left = AVLTree.rotate_left(node.left)
                return AVLTree.rotate_right(node)
        elif balance < -1:
            if key > node.right.key:
                return AVLTree.rotate_left(node)
            else:
                node.right = AVLTree.rotate_right(node.right)
                return AVLTree.rotate_left(node)
        return node

    def insert(self, key):
        self.root = AVLTree.__insert(self.root, key)

    @staticmethod
    def __delete(node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = AVLTree.__delete(node.left, key)
        elif key > node.key:
            node.right = AVLTree.__delete(node.right, key)
        else:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                succ = AVLTree.min_value_node(node.right)
                node.key = succ.key
                node.right = AVLTree.__delete(node.right, succ.key)
            return node

        if node is None:
            return node

        node.update_height()
        balance = node.get_balance()
        if balance > 1:
            if node.left.get_balance() >= 0:
                return AVLTree.rotate_right(node)
            else:
                node.left = AVLTree.rotate_left(node.left)
                return AVLTree.rotate_right(node)
        elif balance < -1:
            if node.right.get_balance() <= 0:
                return AVLTree.rotate_left(node)
            else:
                node.right = AVLTree.rotate_right(node.right)
                return AVLTree.rotate_left(node)
        return node

    def delete(self, key):
        self.root = AVLTree.__delete(self.root, key)

    @staticmethod
    def __search(root, key):
        if root is None or root.key == key:
            return root
        if root.key < key:
            return AVLTree.__search(root.right, key)
        return AVLTree.__search(root.left, key)

    def search(self, key):
        return AVLTree.__search(self.root, key)

    @staticmethod
    def min_value_node(node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def inorder_traversal(self):
        while self.root is not None:
            self.inorder_traversal(self.root.left)
            print(self.root.value),
            self.inorder_traversal(self.root.right)

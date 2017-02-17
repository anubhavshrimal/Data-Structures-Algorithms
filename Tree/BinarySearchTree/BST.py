#!/usr/bin/python3


class Node:
    def __init__(self, data=None, right_child=None, left_child=None, parent=None):
        self.data = data
        self.right_child = right_child
        self.left_child = left_child
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def has_any_children(self):
        return self.right_child or self.left_child

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not(self.right_child or self.left_child)

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def replace_data(self, data):
        self.data = data

    def replace_left_child(self, left_child):
        self.left_child = left_child

    def replace_right_child(self, right_child):
        self.right_child = right_child


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.has_left_child():
                self._insert(data, current_node.left_child)
            else:
                current_node.left_child = Node(data, parent=current_node)
        else:
            if current_node.has_right_child():
                self._insert(data, current_node.right_child)
            else:
                current_node.right_child = Node(data, parent=current_node)

    @staticmethod
    def find_inorder_ancestor(current_node):
        if current_node.has_right_child():
            current_node = current_node.right_child
            while current_node.has_left_child():
                current_node = current_node.left_child
            return current_node

        ancestor = current_node.parent
        child = current_node
        while ancestor is not None and child is ancestor.right_child:
            child = ancestor
            ancestor = child.parent
        return ancestor

    def delete_node(self, data):
        if self.root is None:
            print("No node to delete in the tree")
        else:
            if self._delete(data, self.root) is not None:
                print("Deleted", data)
            else:
                print(data,"not found")

    def _delete(self, data, current_node):
        while current_node is not None and data != current_node.data:
            if data <= current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

        if current_node is not None:
            if current_node.is_leaf():
                if current_node.is_left_child():
                    current_node.parent.left_child = None
                else:
                    current_node.parent.right_child = None
            else:
                successor = self.find_inorder_ancestor(current_node)
                if successor is None:
                    current_node.data = current_node.left_child.data
                    current_node.left_child = None
                else:
                    temp = current_node.data
                    current_node.data = successor.data
                    successor.data = temp
                    self._delete(temp, successor)
            return True
        else:
            return None

    def inorder(self):
        current_node = self.root
        self._inorder(current_node)
        print('End')

    def _inorder(self, current_node):
        if current_node is None:
            return
        self._inorder(current_node.left_child)
        print(current_node.data," -> ",end='')
        self._inorder(current_node.right_child)

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert_node(6)
    tree.insert_node(9)
    tree.insert_node(6)
    tree.insert_node(5)
    tree.insert_node(8)
    tree.insert_node(7)
    tree.insert_node(3)
    tree.insert_node(2)
    tree.insert_node(4)
    tree.inorder()
    tree.delete_node(6)
    tree.delete_node(1)
    tree.delete_node(3)
    tree.inorder()
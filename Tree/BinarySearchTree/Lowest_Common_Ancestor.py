# Find the Lowest Common Ancestor (LCA) in a Binary Search Tree


# A Binary Search Tree node
class Node:
    # Constructor to initialise node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data <= current_node.data:
            if current_node.left is not None:
                self._insert(data, current_node.left)
            else:
                current_node.left = Node(data)
        else:
            if current_node.right is not None:
                self._insert(data, current_node.right)
            else:
                current_node.right = Node(data)

    def inorder(self):
        current_node = self.root
        self._inorder(current_node)
        print('End')

    def _inorder(self, current_node):
        if current_node is None:
            return
        self._inorder(current_node.left)
        print(current_node.data, " -> ", end='')
        self._inorder(current_node.right)


# assuming both nodes are present in the tree
def lca_bst(root, value1, value2):
    while root is not None:
        if value2 > root.data < value1:
            root = root.right
        elif value2 < root.data > value1:
            root = root.left
        else:
            return root.data


if __name__ == '__main__':
    tree = BST()
    tree.insert_node(6)
    tree.insert_node(8)
    tree.insert_node(9)
    tree.insert_node(6)
    tree.insert_node(5)
    tree.insert_node(7)
    tree.insert_node(3)
    tree.insert_node(2)
    tree.insert_node(4)
    print(lca_bst(tree.root, 4, 2))

"""
given tree:
                6
            6          8
        5       7          9
     3
  2     4
"""

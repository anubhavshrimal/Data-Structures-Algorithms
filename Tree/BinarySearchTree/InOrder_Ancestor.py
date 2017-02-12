# find the in-order ancestor of a given node in BST


# A Binary Search Tree node
class Node:
    # Constructor to initialise node
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


def findInOrderAncestor(n):
    if n.right is not None:
        return findMinKeyWithinTree(n.right)

    ancestor = n.parent
    child = n
    while ancestor is not None and child == ancestor.right:
        child = ancestor
        ancestor = child.parent
    return ancestor


def findMinKeyWithinTree(root):
    while root.left is not None:
        root = root.left
    return root


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2, root)
    root.right = Node(6, root)
    root.left.left = Node(1, root.left)
    root.left.right = Node(3, root.left)
    successor = findInOrderAncestor(root.left.right)

    if successor is not None:
        print(successor.data)
    else:
        print("No in order successor")

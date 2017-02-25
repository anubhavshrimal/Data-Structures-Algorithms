# Given a Perfect Binary Tree, reverse the alternate level nodes of the binary tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def reverse_alt_levels(root):
    pre_order_rev(root.left, root.right, 0)


def pre_order_rev(root_left, root_right, level):
    # Base case
    if (root_left or root_right) is None:
        return

    # swap the data of nodes if at an alternate level
    if level % 2 == 0:
        root_left.data, root_right.data = root_right.data, root_left.data

    # go to the next level with left of left root and right of right root
    # and vice versa
    pre_order_rev(root_left.left, root_right.right, level+1)
    pre_order_rev(root_left.right, root_right.left, level+1)


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=' -> ')
    in_order(root.right)


if __name__ == '__main__':
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')
    root.right.right = Node('g')
    root.left.left.left = Node('h')
    root.left.left.right = Node('i')
    root.left.right.left = Node('j')
    root.left.right.right = Node('k')
    root.right.left.left = Node('l')
    root.right.left.right = Node('m')
    root.right.right.left = Node('n')
    root.right.right.right = Node('o')

    print('Before Reversal:')
    in_order(root)
    print()

    # Call the reverse alternate levels function
    reverse_alt_levels(root)

    print('After Reversal:')
    in_order(root)
    print()

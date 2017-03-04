# Remove nodes on root to leaf paths of length < K


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def remove_path_less_than(root, k):
    return remove_path_util(root, 1, k)


def remove_path_util(root, level, k):
    if root is None:
        return None

    root.left = remove_path_util(root.left, level+1, k)
    root.right = remove_path_util(root.right, level+1, k)

    if root.left is None and root.right is None and level < k:
        del root
        return None

    return root


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=' ')
    in_order(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)
    root.right.right = Node(6)
    root.right.right.left = Node(8)
    in_order(root)
    print()
    root = remove_path_less_than(root, 4)
    in_order(root)

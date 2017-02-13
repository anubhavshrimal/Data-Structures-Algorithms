# Find minimum depth of a binary tree
from collections import deque


# A Binary Tree node
class Node:
    # Constructor to initialise node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_min_depth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append((root, 1))

    while queue:
        node, height = queue.popleft()
        if node.left is None and node.right is None:
            return height

        else:
            if node.left is not None:
                queue.append((node.left, height + 1))
        if node.right is not None:
            queue.append((node.right, height + 1))


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(get_min_depth(root))

# Find minimum depth of a binary tree
from collections import deque


# A Binary Tree node
class Node:
    # Constructor to initialise node
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def get_min_depth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append((root, 1))

    while queue:
        node, height = queue.popleft()
        if node.left_child is None and node.right_child is None:
            return height

        else:
            if node.left_child is not None:
                queue.append((node.left_child, height + 1))
        if node.right_child is not None:
            queue.append((node.right_child, height + 1))


if __name__ == '__main__':
    root = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)

    print(get_min_depth(root))

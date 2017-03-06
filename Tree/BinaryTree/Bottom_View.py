# Print Nodes in Bottom View of Binary Tree
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bottom_view(root):
    if root is None:
        return

    # make an empty queue for BFS
    q = deque()

    # dict to store bottom view keys
    bottomview = {}

    # append root in the queue with horizontal distance as 0
    q.append((root, 0))

    while q:
        # get the element and horizontal distance
        elem, hd = q.popleft()

        # update the last seen hd element
        bottomview[hd] = elem.data

        # add left and right child in the queue with hd - 1 and hd + 1
        if elem.left is not None:
            q.append((elem.left, hd - 1))
        if elem.right is not None:
            q.append((elem.right, hd + 1))

    # return the bottomview
    return bottomview


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    bottomview = bottom_view(root)
    
    for i in sorted(bottomview):
        print(bottomview[i], end=' ')

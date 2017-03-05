# Print Nodes in Top View of Binary Tree
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def top_view(root):
    if root is None:
        return

    # make an empty queue for BFS
    q = deque()

    # empty set
    sets = set({})

    # list to store top view keys
    topview = []

    # append root in the queue with horizontal distance as 0
    q.append((root, 0))

    while q:
        # get the element and horizontal distance
        elem, hd = q.popleft()

        # if the hd is seen first time it will be top view
        if hd not in sets:
            topview.append((elem.data, hd))
            sets.add(hd)

        # add left and right child in the queue with hd - 1 and hd + 1
        if elem.left is not None:
            q.append((elem.left, hd - 1))
        if elem.right is not None:
            q.append((elem.right, hd + 1))

    # return the sorted topview on the basis of hd
    return sorted(topview, key=lambda x: x[1])


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)

    for i in top_view(root):
        print(i[0], end=' ')

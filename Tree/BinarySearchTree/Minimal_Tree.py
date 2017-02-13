# Given a sorted array, create a binary search tree with minimal height


# A Binary Tree node
class Node:
    # Constructor to initialise node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def make_minimal_bst(arr, start, end):
    if end < start:
        return None
    mid = int((start + end) / 2)
    root = Node(arr[mid])

    root.left = make_minimal_bst(arr, start, mid-1)
    root.right = make_minimal_bst(arr, mid+1, end)

    return root


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data, end=' -> ')
    in_order(root.right)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    root = make_minimal_bst(arr, 0, len(arr)-1)
    in_order(root)
    print('end')

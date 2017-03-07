# Check whether a binary tree is a full binary tree or not


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_full_bt(root):
    # If tree is empty
    if root is None:
        return True

    # if both child are None
    if root.left is None and root.right is None:
        return True

    # if the node has both children and both sub tree are full binary trees
    if root.left is not None and root.right is not None:
        return check_full_bt(root.left) and check_full_bt(root.right)

    return False

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    root.left.right = Node(40)
    root.left.left = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    root.left.left.left = Node(80)
    root.left.left.right = Node(90)
    root.left.right.left = Node(80)
    root.left.right.right = Node(90)
    root.right.left.left = Node(80)
    root.right.left.right = Node(90)
    root.right.right.left = Node(80)
    root.right.right.right = Node(90)

    if check_full_bt(root):
        print('Yes, given binary tree is Full BT')
    else:
        print('No, given binary tree is not Full BT')

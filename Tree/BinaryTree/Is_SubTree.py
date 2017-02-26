# Given two binary trees, check if the first tree is subtree of the second one.


# A Binary Tree node
class Node:
    # Constructor to initialise node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def store_in_order(root, arr):
    if root is None:
        arr.append('$')
        return
    store_in_order(root.left, arr)
    arr.append(root.data)
    store_in_order(root.right, arr)


def store_pre_order(root, arr):
    if root is None:
        arr.append('$')
        return
    store_pre_order(root.left, arr)
    store_pre_order(root.right, arr)
    arr.append(root.data)


def isSubTree(t1, t2):
    order_t1 = []
    order_t2 = []

    store_in_order(t1, order_t1)
    store_in_order(t2, order_t2)
    if ''.join(order_t1).find(''.join(order_t2)) == -1:
        return False

    order_t1 = []
    order_t2 = []

    store_pre_order(t1, order_t1)
    store_pre_order(t2, order_t2)
    if ''.join(order_t1).find(''.join(order_t2)) == -1:
        return False

    return True


T = Node('a')
T.left = Node('b')
T.right = Node('d')
T.left.left = Node('c')
T.left.right = Node('e')

S = Node('b')
S.left = Node('c')
S.right = Node('e')

if isSubTree(T, S):
    print('Yes, S is a subtree of T')
else:
    print('No, S is not a subtree of T')

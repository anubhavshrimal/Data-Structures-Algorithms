""" Program to find LCA of n1 and n2 using one traversal of
 Binary tree
"""


# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# This function returns reference to LCA of two given values n1 and n2
# v1 is set as true by this function if n1 is found
# v2 is set as true by this function if n2 is found
def findLCAUtil(root, n1, n2, v):
    # Base Case
    if root is None:
        return None

    # IF either n1 or n2 matches ith root's key, report
    # the presence by setting v1 or v2 as true and return
    # root
    if root.key == n1:
        v[0] = True
        return root

    if root.key == n2:
        v[1] = True
        return root

    # Look for keys in left and right subtree
    left_lca = findLCAUtil(root.left, n1, n2, v)
    right_lca = findLCAUtil(root.right, n1, n2, v)

    # if one key is present in left subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca


def find(root, k):
    # Base Case
    if root is None:
        return False

    # If key is present at root, or if left subtree or right
    # subtree , return true
    if (root.key == k or find(root.left, k) or
            find(root.right, k)):
        return True

    # Else return false
    return False


# This function returns LCA of n1 and n2 only if both
# n1 and n2 are present in tree, otherwise returns None
def findLCA(root, n1, n2):
    # Initialize n1 and n2 as not visited
    v = [False, False]

    # Find lca of n1 and n2
    lca = findLCAUtil(root, n1, n2, v)

    # Returns LCA only if both n1 and n2 are present in tree
    if v[0] and v[1] or v[0] and find(lca, n2) or v[1] and find(lca, n1):
        return lca

    # Else return None
    return None


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

lca = findLCA(root, 4, 5)

if lca is not None:
    print("LCA(4, 5) = ", lca.key)
else:
    print("Keys are not present")

lca = findLCA(root, 4, 10)
if lca is not None:
    print("LCA(4,10) = ", lca.key)
else:
    print("Keys are not present")

    # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
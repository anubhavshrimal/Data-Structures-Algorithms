# Check if a binary tree is height balanced
# abs(height[leftTree] - height[rightTree]) <= 1


# A Binary Tree node
class Node:
    # Constructor to initialise node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_height(root):
    if root is None:
        return -1
    left_height = check_height(root.left)
    if left_height is float('inf'):
        return float('inf')

    right_height = check_height(root.right)
    if right_height is float('inf'):
        return float('inf')

    height = abs(left_height - right_height)
    if height > 1:
        return float('inf')
    else:
        return max(left_height, right_height) + 1


def isBalanced(root):
    return check_height(root) != float('inf')

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    if isBalanced(root):
        print("Yes! the tree is balanced")
    else:
        print("No! the tree is not balanced")
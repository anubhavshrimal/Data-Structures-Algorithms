# find the maximum path sum. The path may start and end at any node in the tree.

class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_sum_path(root):
    max_sum_path_util.res = -float('inf')

    max_sum_path_util(root)
    return max_sum_path_util.res


def max_sum_path_util(root):
    if root is None:
        return 0
    # find max sum in left and right sub tree
    left_sum = max_sum_path_util(root.left)
    right_sum = max_sum_path_util(root.right)

    # if current node is one of the nodes in the path above for max
    # it can either be along, or with left sub tree or right sub tree
    max_single = max(max(left_sum, right_sum) + root.data, root.data)

    # if the current root itself is considered as top node of the max path
    max_parent = max(left_sum + right_sum + root.data, max_single)

    # store the maximum result
    max_sum_path_util.res = max(max_sum_path_util.res, max_parent)

    # return the max_single for upper nodes calculation
    return max_single


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)

    print('max path sum is:', max_sum_path(root))



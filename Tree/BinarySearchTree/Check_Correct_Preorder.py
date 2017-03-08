# Check if a given array can represent Preorder Traversal of Binary Search Tree


def check_pre_order(arr):
    minimum = -float('inf')

    stack = []

    for val in arr:
        if val < minimum:
            return False

        while len(stack) != 0 and stack[-1] < val:
            minimum = stack.pop()

        stack.append(val)

    return True


if __name__ == '__main__':
    pre_order = [40, 30, 35, 80, 100]
    print("Valid Preorder" if check_pre_order(pre_order) else "Invalid Preorder")
    pre_order = [40, 30, 35, 20, 80, 100]
    print("Valid Preorder" if check_pre_order(pre_order) else "Invalid Preorder")



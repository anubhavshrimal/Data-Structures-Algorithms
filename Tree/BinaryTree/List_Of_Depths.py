# Create a list of all nodes at each depth

# A Binary Tree node
class Node:
    # Constructor to initialise node
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def list_of_depths(root):
    if root is None:
        return []
    depths = []
    q = []
    q.append(root)

    while q:
        parents = q
        depths.append(q)
        q = []
        for parent in parents:
            if parent.left_child is not None:
                q.append(parent.left_child)
            if parent.right_child is not None:
                q.append(parent.right_child)

    return depths

if __name__ == '__main__':
    root = Node(1)
    root.left_child = Node(2)
    root.right_child = Node(3)
    root.left_child.left_child = Node(4)
    root.left_child.right_child = Node(5)

    for depth, list_nodes in enumerate(list_of_depths(root)):
        print('Depth', depth, end=': ')
        for n in list_nodes:
            print(n.data, end=' -> ')
        print('end')

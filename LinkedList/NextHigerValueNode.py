# Python program to Point to next higher value node in a linked list with an arbitrary pointer


# Node class
class Node:

    # Constructor to initialise data and next and arbitrary pointer
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.arbit = None


class SinglyLinkedList:

    # Constructor to initialise head
    def __init__(self, head=None):
        self.head = head

    # Function to Insert data at the beginning of the linked list
    def insert_at_beg(self, data):
        node = Node(data)
        node.next = self.head
        node.arbit = node.next
        self.head = node

    # Function to print the linked list
    def print_data(self):
        current = self.head
        # print data of each node
        while current is not None:
            print(current.data, '-> ', end='')
            current = current.next

        current = self.head
        print('None')
        while current is not None:
            print("V", '   ', end='')
            current = current.next

        current = self.head
        print()
        # print arbitrary pointer node's data of each node
        while current is not None:
            if current.arbit is not None:
                print(current.arbit.data, '   ', end='')
            else:
                print("N", '   ', end='')
            current = current.next
        print()


# Function to split the linked list into two halves
def split(head):
    slow = head

    if slow is None or slow.arbit is None:
        return head, None

    fast = slow.arbit

    # Reach to the middle of the linked list
    while fast is not None:
        fast = fast.arbit
        if fast is not None:
            fast = fast.arbit
            slow = slow.arbit

    fast = slow.arbit
    # break the linked list in half
    slow.arbit = None

    # return the 2 linked lists formed
    return head, fast


# Function to merge linked lists in sorted order
def merge(a, b):
    # Make a dummy node
    dummy = Node()
    # dummy node arbit will be the head of our merged list
    dummy.arbit = None

    temp = SinglyLinkedList(dummy)
    tail = temp.head

    while True:
        if a is None:
            tail.arbit = b
            break
        elif b is None:
            tail.arbit = a
            break
        elif a.data <= b.data:
            tail.arbit = a
            a = a.arbit
        else:
            tail.arbit = b
            b = b.arbit
        tail = tail.arbit

    return temp.head.arbit


# Function Merge Sort
def merge_sort(head):

    if head is None or head.arbit is None:
        return head

    a, b = split(head)
    a = merge_sort(a)
    b = merge_sort(b)

    head = merge(a, b)

    return head


if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list.insert_at_beg(3)
    linked_list.insert_at_beg(2)
    linked_list.insert_at_beg(10)
    linked_list.insert_at_beg(5)

    # before linking the arbit
    print('before linking')
    linked_list.print_data()

    # call merge_sort function
    # to sort the linked list on the basis of the arbitrary pointers
    merge_sort(linked_list.head)

    # after linking the arbit
    print('after linking')
    linked_list.print_data()

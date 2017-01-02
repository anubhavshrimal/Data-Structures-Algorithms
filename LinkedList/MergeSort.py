# Python program to perform Merge Sort on a Signly linked list


# Node class
class Node:

    # Constructor to initialise data and next
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:

    # Constructor to initialise head
    def __init__(self):
        self.head = None

    # Function to Insert data at the beginning of the linked list
    def insert_at_beg(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # Function to print the linked list
    def print_data(self):
        current = self.head
        while current is not None:
            print(current.data, '-> ', end='')
            current = current.next
        print('None')


# Function to split the linked list into two halves
def split(head):
    slow = head

    if slow is None or slow.next is None:
        return head, None

    fast = slow.next

    while fast is not None:
        fast = fast.next
        if fast is not None:
            fast = fast.next
            slow = slow.next

    fast = slow.next
    slow.next = None

    return head, fast


# Function to merge linked lists
def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if a.data < b.data:
        a.next = merge(a.next, b)
        return a
    else:
        b.next = merge(b.next, a)
        return b


# Function Merge Sort
def merge_sort(head):

    if head is None or head.next is None:
        return head

    a, b = split(head)
    a = merge_sort(a)
    b = merge_sort(b)

    head = merge(a, b)

    return head

if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list.insert_at_beg(9)
    linked_list.insert_at_beg(3)
    linked_list.insert_at_beg(2)
    linked_list.insert_at_beg(1)
    linked_list.insert_at_beg(5)
    linked_list.insert_at_beg(4)
    linked_list.insert_at_beg(8)
    linked_list.insert_at_beg(7)
    linked_list.insert_at_beg(6)


    # before sorting
    print('before sorting')
    linked_list.print_data()

    # call merge_sort function
    linked_list.head = merge_sort(linked_list.head)

    #after sorting
    print('after sorting')
    linked_list.print_data()

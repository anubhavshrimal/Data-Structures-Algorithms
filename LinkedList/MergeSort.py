# Python program to perform Merge Sort on a Signly linked list


# Node class
class Node:

    # Constructor to initialise data and next
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:

    # Constructor to initialise head
    def __init__(self, head=None):
        self.head = head

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

    # Reach to the middle of the linked list
    while fast is not None:
        fast = fast.next
        if fast is not None:
            fast = fast.next
            slow = slow.next

    fast = slow.next
    # break the linked list in half
    slow.next = None

    # return the 2 linked lists formed
    return head, fast


# Function to merge linked lists in sorted order
def merge(a, b):
    # Make a dummy node
    dummy = Node()
    # dummy node next will be the head of our merged list
    dummy.next = None

    temp = SinglyLinkedList(dummy)
    tail = temp.head

    while True:
        if a is None:
            tail.next = b
            break
        elif b is None:
            tail.next = a
            break
        elif a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    return temp.head.next


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

    # after sorting
    print('after sorting')
    linked_list.print_data()

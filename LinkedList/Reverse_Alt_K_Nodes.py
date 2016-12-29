# Python program to alternately reverse a linked list in group of given size k


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

    # Function to reverse K nodes of linked list
    def reverse_k_nodes(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        # traverse k nodes ahead reversing the links or until current is not None
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if head is not None:
            head.next = current

        count = 0
        # traverse the k nodes to be skipped
        while current is not None and count < k-1:
            current = current.next
            count += 1

        # recursive call to the function to alternate reverse the remaining n-2k nodes
        if current is not None:
            current.next = self.reverse_k_nodes(current.next, k)

        # return the new header of the current sublist
        return prev

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

if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list.insert_at_beg(10)
    linked_list.insert_at_beg(9)
    linked_list.insert_at_beg(8)
    linked_list.insert_at_beg(7)
    linked_list.insert_at_beg(6)
    linked_list.insert_at_beg(5)
    linked_list.insert_at_beg(4)
    linked_list.insert_at_beg(3)
    linked_list.insert_at_beg(2)
    linked_list.insert_at_beg(1)
    linked_list.print_data()
    # call the reverse k nodes function
    linked_list.head = linked_list.reverse_k_nodes(linked_list.head, 3)
    # print the reversed list
    linked_list.print_data()

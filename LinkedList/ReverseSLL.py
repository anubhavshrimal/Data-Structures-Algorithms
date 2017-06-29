# Python program to reverse a singly linked list


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

    # Function to reverse a linked list
    def reverse(self):

        # If linked list is empty
        if self.head is None:
            return None

        current = self.head
        prev = None

        while current is not None:
            # Store the value of current.next
            next = current.next
            # Set current.next to point to the previous node
            current.next = prev
            # Update pointers for next iteration
            prev = current
            current = next

        self.head = prev

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
    linked_list.insert_at_beg(7)
    linked_list.insert_at_beg(6)
    linked_list.insert_at_beg(5)
    linked_list.insert_at_beg(4)
    linked_list.insert_at_beg(3)
    linked_list.insert_at_beg(2)
    linked_list.insert_at_beg(1)
    linked_list.print_data()
    # call the reverse function
    linked_list.reverse()
    # print the reversed list
    linked_list.print_data()

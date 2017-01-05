# Python program to Merge a linked list into another linked list at alternate positions


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

    # Function to merge 2 linked lists at alternate positions
    def merge(self, l2):
        h1 = self.head
        h2 = l2.head

        # Merge at alternate positions until the h1 has alternate positions
        while h1 and h2 is not None:
            h1_next = h1.next
            h2_next = h2.next

            h1.next = h2
            h2.next = h1_next

            h1 = h1_next
            h2 = h2_next

        # update the head of h2 if linked list remains i.e. no more alternate positions in h1
        l2.head = h2

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
    linked_list1 = SinglyLinkedList()
    linked_list1.insert_at_beg(9)
    linked_list1.insert_at_beg(8)
    linked_list1.insert_at_beg(7)
    linked_list1.insert_at_beg(6)
    linked_list1.insert_at_beg(5)

    linked_list2 = SinglyLinkedList()
    linked_list2.insert_at_beg(12)
    linked_list2.insert_at_beg(11)
    linked_list2.insert_at_beg(10)
    linked_list2.insert_at_beg(4)
    linked_list2.insert_at_beg(3)
    linked_list2.insert_at_beg(2)
    linked_list2.insert_at_beg(1)

    print('List 1:')
    linked_list1.print_data()
    print('List 2:')
    linked_list2.print_data()

    # call the merge function
    linked_list1.merge(linked_list2)

    # print the merged linked list
    print('Merged list:')
    linked_list1.print_data()
    linked_list2.print_data()

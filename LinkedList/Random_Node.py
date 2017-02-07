# to select a random node in a singly linked list
import random


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

    # Function to get random node in linked list
    def get_random_node(self):
        if self.head is None:
            return None

        random.seed()
        random_node = self.head
        current = self.head.next
        n = 2
        while current is not None:
            if random.randrange(n) == 0:
                random_node = current
            current = current.next
            n += 1
        return random_node

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
    linked_list.insert_at_beg(9)
    linked_list.insert_at_beg(8)
    linked_list.insert_at_beg(7)
    linked_list.insert_at_beg(6)
    linked_list.insert_at_beg(5)
    linked_list.insert_at_beg(4)
    linked_list.insert_at_beg(3)
    linked_list.insert_at_beg(2)
    linked_list.insert_at_beg(1)

    random_node = linked_list.get_random_node()
    print("Random node data is:")
    print(random_node.data)

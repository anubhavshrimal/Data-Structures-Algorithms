#!/usr/bin/python3


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, node):
        self.next = node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        size = 0

        while current is not None:
            size += 1
            current = current.get_next()
        return size

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.get_next() is not None:
                current = current.get_next()

            current.set_next(node)
        self.print_data()

    def insert_at_beg(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node
        self.print_data()

    def delete_from_end(self):
        current = self.head
        previous = None

        if current is None:
            print("Linked List Underflow!!")
        else:
            while current.get_next() is not None:
                previous = current
                current = current.get_next()

            if previous is None:
                self.head = None
            else:
                previous.set_next(None)
        self.print_data()

    def delete_from_beg(self):
        current = self.head

        if current is None:
            print("Linked List Underflow!!")
        else:
            self.head = current.get_next()
        self.print_data()

    def is_empty(self):
        return self.head is None

    def print_data(self):
        current = self.head

        while current is not None:
            print(current.get_data(), '->', end='')
            current = current.get_next()
        print('End of list')


linked_list = SinglyLinkedList()
linked_list.insert_at_beg(3)
linked_list.insert_at_beg(2)
linked_list.insert_at_beg(1)
linked_list.insert_at_end(4)
linked_list.insert_at_end(5)
linked_list.delete_from_beg()
linked_list.delete_from_end()
print("size: ", linked_list.size())

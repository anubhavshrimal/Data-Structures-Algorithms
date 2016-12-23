# Python program to skip M nodes and then delete N nodes alternately in a singly linked list


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

    # Function to skip M delete N nodes
    def skip_m_delete_n(self, m, n):
        current = self.head

        # if list is empty return
        if current is None:
            return

        # Main loop to traverse the whole list
        while current is not None:
            # loop to skip M nodes
            for i in range(1, m):
                if current is None:
                    return
                current = current.next

            if current is None:
                return

            # loop to delete N nodes
            temp = current.next
            for i in range(1, n+1):
                if temp is None:
                    break
                temp = temp.next

            # Point the last node skipped to the node after N nodes deletion
            current.next = temp
            # set current for next iteration
            current = temp

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

    linked_list.print_data()

    # call the skip_m_delete_n function
    linked_list.skip_m_delete_n(2, 2)

    # print the modified linked list
    linked_list.print_data()

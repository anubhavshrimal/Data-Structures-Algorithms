# Python program to check if the singly linked list contains cycle or not


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

    # Function to find cycle in linked list
    def find_cycle(self):
        fast = self.head.next
        slow = self.head

        # Make fast run twice the speed of slow
        # if fast coincide with slow
        # then there is a loop or cycle
        while fast is not None:
            # return True if cycle
            if fast is slow:
                return True
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next

        # return False if no cycle
        return False

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

    temp = head = linked_list.head

    # get pointer to the end of the list
    while temp.next is not None:
        temp = temp.next

    # Make a loop in the list
    temp.next = head.next.next.next

    # call the find_cycle function
    result = linked_list.find_cycle()

    # print if cycle or not
    print('Yes! there is a cycle') if result else print('No! there is no cycle')



# Python program to Clone a linked list with next and random pointer


# Node class
class Node:

    # Constructor to initialise data and next
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.random = None

class SinglyLinkedList:

    # Constructor to initialise head
    def __init__(self, head=None):
        self.head = None

    # Function to create copy the linked list
    def copy_list(self, l2):
        # if first list is empty return
        if self.head is None:
            return

        curr1 = self.head

        # insert new nodes with same data as linst at adjacent positions of each node
        while curr1 is not None:
            node = Node(curr1.data)
            temp = curr1.next
            curr1.next = node
            node.next = temp
            curr1 = temp

        curr1 = self.head
        # update the random pointers of even node to point to the random nodes of odd nodes next
        while curr1 is not None:
            if curr1.random is not None:
                curr1.next.random = curr1.random.next
            curr1 = curr1.next.next

        curr1 = self.head
        curr2 = l2.head
        # assign even nodes to the Copy linked list to make the new list
        # re-assign the old links of list 1
        while curr1 is not None:
            if l2.head is None:
                l2.head = curr1.next
                curr2 = l2.head
            else:
                curr2.next = curr1.next
                curr2 = curr2.next
            curr1.next = curr1.next.next
            curr2.next = None
            curr1 = curr1.next



    # Function to Insert data at the beginning of the linked list
    def insert_at_beg(self, data):
        node = Node(data)
        node.next = self.head
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
        # print random pointer node's data of each node
        while current is not None:
            if current.random is not None:
                print(current.random.data, '   ', end='')
            else:
                print("N", '   ', end='')
            current = current.next
        print()

if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    # make nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    # set next pointer of each node
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # set random pointer of each node
    node1.random = node3
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node2
    # assing the nodes list to head
    linked_list.head = node1

    # print the data of linked list
    print('original list:')
    linked_list.print_data()

    # make empty LL2 to copy data of LL1 in
    linked_list2 = SinglyLinkedList(Node())

    # copy LL1 into LL2
    linked_list.copy_list(linked_list2)

    # print the copied linked list
    print('copied list:')
    linked_list2.print_data()
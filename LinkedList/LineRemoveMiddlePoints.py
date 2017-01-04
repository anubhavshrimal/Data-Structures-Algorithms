"""Given a linked list of co-ordinates where adjacent points either form a vertical line or a horizontal line.
Delete points from the linked list which are in the middle of a horizontal or vertical line."""
"""Input:  (0,10)->(1,10)->(5,10)->(7,10)
                                  |
                                (7,5)->(20,5)->(40,5)
Output: Linked List should be changed to following
        (0,10)->(7,10)
                  |
                (7,5)->(40,5) """


# Node class
class Node:

    # Constructor to initialise (x, y) coordinates and next
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        self.next = None


class SinglyLinkedList:

    # Constructor to initialise head
    def __init__(self):
        self.head = None

    # Function to find middle node of a linked list
    def delete_middle_nodes(self):
        current = self.head

        # iterate while the next of the next node is not none
        while current and current.next and current.next.next is not None:
            # assign variables for next and next of next nodes
            next = current.next
            next_next = current.next.next

            # if x coordinates are equal of current and next node i.e. horizontal line
            if current.x == next.x:
                # check if there are more than 2 nodes in the horizontal line
                # if yes then delete the middle node and update next and next_next
                while next_next is not None and next.x == next_next.x:
                    current.next = next_next
                    next = next_next
                    next_next = next_next.next
            # if y coordinates are equal of current and next node i.e. vertical line
            elif current.y == next.y:
                # check if there are more than 2 nodes in the vertical line
                # if yes then delete the middle node and update next and next_next
                while next_next is not None and next.y == next_next.y:
                    current.next = next_next
                    next = next_next
                    next_next = next_next.next
            # updated the current node to next node for checking the next line nodes
            current = current.next

    # Function to Insert data at the beginning of the linked list
    def insert_at_beg(self, x, y):
        node = Node(x, y)
        node.next = self.head
        self.head = node

    # Function to print the linked list
    def print_data(self):
        current = self.head
        while current is not None:
            print('(',current.x, ',', current.y, ') -> ', end='')
            current = current.next
        print('None')

if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list.insert_at_beg(40,5)
    linked_list.insert_at_beg(20,5)
    linked_list.insert_at_beg(7,5)
    linked_list.insert_at_beg(7,10)
    linked_list.insert_at_beg(5,10)
    linked_list.insert_at_beg(1,10)
    linked_list.insert_at_beg(0,10)

    # print the linked list representing vertical and horizontal lines
    linked_list.print_data()

    # call the delete_middle_nodes function
    linked_list.delete_middle_nodes()

    # print the new linked list
    linked_list.print_data()
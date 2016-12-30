# Python program to segregate Even and Odd value nodes in a singly linked list


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

    # Function to segregate even odd value nodes of linked list
    def segregateEvenOdd(self):
        current = None
        prev = self.head
        pivot = None

        # If empty list or single element in the list
        if self.head is None or self.head.next is None:
            return self.head

        # if the first node is even
        # initialise pivot as head
        if prev.data % 2 == 0:
            pivot = self.head
            current = prev.next
        # else find the first node in the list that is even
        # make that node the head of the list
        # initialise pivot as head
        else:
            while prev.next is not None:
                if prev.next.data % 2 == 0:
                    pivot = prev.next
                    prev.next = pivot.next
                    pivot.next = self.head
                    self.head = pivot
                    current = prev.next
                    break
                prev = prev.next

        # keep moving the current pointer and prev pointer
        while current is not None:
            # if even value is found at the node
            if current.data % 2 == 0:
                # if the node is adjacent to pivot
                # simply increment the pivot to next node
                # and shift prev and current one step ahead
                if prev is pivot:
                    pivot = current
                    prev = current
                    current = current.next
                # else insert the node after the pivot
                # shift the pivot to the newly inserted node
                # update current and prev
                else:
                    prev.next = current.next
                    current.next = pivot.next
                    pivot.next = current
                    pivot = current
                    current = prev.next
            # if odd value simply increment current and prev
            else:
                prev = current
                current = current.next

        # return the updated linked list head
        return self.head

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
    linked_list.insert_at_beg(2)
    linked_list.insert_at_beg(3)
    linked_list.insert_at_beg(2)
    print('Before segregation:', end=' ')
    linked_list.print_data()
    linked_list.head = linked_list.segregateEvenOdd()
    print('After segregation:', end=' ')
    linked_list.print_data()
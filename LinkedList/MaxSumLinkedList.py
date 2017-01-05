# Python program to Construct a Maximum Sum Linked List out of two Sorted Linked Lists having some Common nodes.

"""When constructing the result list, we may switch to the other input list only at the point of intersection
(which mean the two node with the same value in the lists). You are allowed to use O(1) extra space."""


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

    # Function to find max sum linked list using 2 linked lists
    def max_sum_list(self, l2):
        pre1 = cur1 = self.head
        pre2 = cur2 = l2.head
        result = None

        # while any of the lists are not empty keep traversing
        while cur1 or cur2 is not None:
            sum1 = sum2 = 0
            while cur1 and cur2 is not None and cur1.data != cur2.data:

                # if 1st list's node data is less than 2nd list's node
                if cur1.data < cur2.data:
                    sum1 += cur1.data
                    cur1 = cur1.next

                # if 2nd list's node data is less than 1st list's node
                else:
                    sum2 += cur2.data
                    cur2 = cur2.next

            # if any of the list has ended calculate the sum of the other list till the end
            if cur1 is None:
                while cur2 is not None:
                    sum2 += cur2.data
                    cur2 = cur2.next
            elif cur2 is None:
                while cur1 is not None:
                    sum1 += cur1.data
                    cur1 = cur1.next

            # initial case when result's head needs to be set
            if pre1 is self.head and pre2 is l2.head:
                result = pre1 if sum1 > sum2 else pre2
            else:
                if sum1 > sum2:
                    pre2.next = pre1.next
                else:
                    pre1.next = pre2.next

            pre1 = cur1
            pre2 = cur2

            if cur1 is not None:
                cur1 = cur1.next
            if cur2 is not None:
                cur2 = cur2.next

        return result

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
    linked_list1.insert_at_beg(130)
    linked_list1.insert_at_beg(120)
    linked_list1.insert_at_beg(100)
    linked_list1.insert_at_beg(90)
    linked_list1.insert_at_beg(32)
    linked_list1.insert_at_beg(12)
    linked_list1.insert_at_beg(3)
    linked_list1.insert_at_beg(0)

    linked_list2 = SinglyLinkedList()
    linked_list2.insert_at_beg(120)
    linked_list2.insert_at_beg(110)
    linked_list2.insert_at_beg(90)
    linked_list2.insert_at_beg(30)
    linked_list2.insert_at_beg(3)
    linked_list2.insert_at_beg(1)

    print('List 1:')
    linked_list1.print_data()
    print('List 2:')
    linked_list2.print_data()

    # call the max_sum_list function and update the list 1's head to point the max sum list
    linked_list1.head = linked_list1.max_sum_list(linked_list2)

    # print the max sum linked list
    print('Max sum linked list:')
    linked_list1.print_data()









# to select a random node in a singly linked list
import random


def get_random_node(head):
    if head is None:
        return None

    random.seed()
    random_node = head
    current = head.next
    n = 2
    while current is not None:
        if random.randrange(n) == 0:
            random_node = current
        current = current.next
        n += 1
    return random_node


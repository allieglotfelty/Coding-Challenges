class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))

class LinkedList(object):
    """LinkedList Class"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, data):
        """Add a node to the end of the list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def print_linked_list(self):
        """Print all items in the list."""

        current = self.head

        while current is not None:
            print current.data
            current = current.next


def add_linked_lists(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """

    rev_l1 = l1.as_rev_string()
    rev_l2 = l2.as_rev_string()
    total = str(int(rev_l1) + int(rev_l2))
    total = list(total)
    new_total = "".join(reversed(total))
    added_ll = LinkedList()

    for num in new_total:
        added_ll.append(num)

    return added_ll

ll1 = Node(3, Node(2, Node(1)))
ll2 = Node(6, Node(5, Node(4)))

added_list = add_linked_lists(ll1, ll2)
added_list.print_linked_list()
# print ll1.as_rev_string()

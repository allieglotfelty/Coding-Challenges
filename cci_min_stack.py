"""Question 3.2 in Cracking the Coding Interview. How would you design a stack
which, in addition to push and pop, has a function min which returns the minimum
element? Push, pop and min should all operate in O(1) time."""

class MinStack(object):
    """A class to implement min stack."""

    def __init__(self):
        """Initialize the min stack."""
        self._list = []
        self._min = []

    def push(self, item):
        """Adds an item to the top of the min stack."""

        self._list.append(item)

        if not self._min or self._min[-1] >= item:
            self._min.append(item)

    def pop(self):
        """Removes an item from the top of the min stack."""

        removed = self._list.pop()

        if removed == self._min[-1]:
            self._min.pop()

        return removed

    def peek(self):
        """Reveals the top item in the min stack."""

        return self._list[-1]

    def is_empty(self):
        """Returns True or False depending on whether the min stack is empty."""

        return self._list == []

    def min(self):
        """Returns the smallest item in the min stack."""

        return self._min[-1]

    def print_stack(self):
        """Prints the stack from bottom to top."""

        print "bottom ----> top", self._list



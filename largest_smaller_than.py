"""Return index of largest num in sorted list that is smaller than given num.

For example:

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
    2

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
    4

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
    1

Never find xnumber --- it's not smaller than itself!

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
    1

If no such number exists, return None:

    >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
    True

"""


def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""

    high_index = len(nums) - 1
    low_index = 0

    if nums[high_index] < xnumber:
        return high_index

    elif nums[low_index] > xnumber:
        return None

    while True:
        midpoint = (high_index - low_index) / 2
        if nums[midpoint] < xnumber and nums[midpoint + 1] >= xnumber:
            return midpoint
        elif nums[midpoint] < xnumber:
            low_index = midpoint
        else:
            high_index = midpoint



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU ARE THE MAXIMUM!\n"


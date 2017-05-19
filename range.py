"""Given list of numbers, return smallest & largest number as a tuple.

For example::

    >>> find_range([3, 4, 2, 5, 10])
    (2, 10)

    >>> find_range([43, 3, 44, 20, 2, 1, 100])
    (1, 100)

For an empty list, it should return `None` as both smallest and largest::

    >>> find_range([])
    (None, None)

Make sure it works with a list of one item, which is both smallest and
largest::

    >>> find_range([7])
    (7, 7)
"""


def find_range(nums):
    """Given list of numbers, return smallest & largest number as a tuple."""

    if not nums:
        return (None, None)

    return (min(nums), max(nums))

    # ALTERNATE SOLUTION:
    # if not nums:
    #     return(None, None)

    # nums.sort()
    # return(nums[0], nums[-1])

    # ALTERNATE SOLUTION:
    # low = None
    # high = None
    # for num in nums:
    #     if low is None or num < low:
    #         low = num
    #     if high is None or num > high:
    #         high = num

    # return (low, high)



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"

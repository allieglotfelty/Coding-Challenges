"""Sum a list of integers.

Given a list of numbers, return the sum. Do not use the built in 'sum' method.

For example::

    >>> sum_list([5, 5])
    10

    >>> sum_list([-5, 10, 4])
    9

    >>> sum_list([20])
    20

The sum of an empty list is zero::

    >>> sum_list([])
    0

"""


def sum_list(num_list):
    """Return the sum of all numbers in list."""

    return reduce(lambda x, y: x+y, num_list, 0)


    # ALTERNATE SOLUTION 1:

    # return sum(num_list)

    

    # ALTERNATE SOLUTION 2:

    # total = 0

    # for num in num_list:
    #     total += num

    # return total


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. BOOYA!!\n"

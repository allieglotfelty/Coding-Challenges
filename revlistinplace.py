"""Reverse list in place.

You cannot do this with reversed(), .reverse(), or list slice
assignment!

    >>> lst = []
    >>> rev_list_in_place(lst)
    >>> lst
    []

    >>> lst = ['a']
    >>> rev_list_in_place(lst)
    >>> lst
    ['a']

    >>> lst = [1, 2, 3]
    >>> rev_list_in_place(lst)
    >>> lst
    [3, 2, 1]

    >>> lst = [1, 2, 3, 4]
    >>> rev_list_in_place(lst)
    >>> lst
    [4, 3, 2, 1]
"""


def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """

    if len(lst) < 2:
        return

    mid_index = len(lst)/2
    if len(lst) % 2 == 0:
        high_pointer = mid_index
        low_pointer = mid_index - 1
    else:
        high_pointer = mid_index + 1
        low_pointer = mid_index - 1

    while high_pointer < len(lst):
        high = lst[high_pointer]
        low = lst[low_pointer]
        lst[high_pointer] = low
        lst[low_pointer] = high
        high_pointer += 1
        low_pointer -= 1


    # rev_lst = []
    # index = -1
    # while lst:
    #     last_item = lst.pop()
    #     rev_lst.append(last_item)
    
    # for i in range(len(lst)):





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE THE BEST!\n"

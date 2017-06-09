"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """
    # [3, 5, 7], [2, 6, 8, 10]
    # comb = [1]

    combined_lists_sorted = []

    while len(a) or len(b):
        if not len(a):
            combined_lists_sorted.append(b.pop(0))
            continue
        if not len(b):
            combined_lists_sorted.append(a.pop(0))
            continue
        if a[0] <= b[0]:
            combined_lists_sorted.append(a.pop(0))
        else:
            combined_lists_sorted.append(b.pop(0))

    return combined_lists_sorted


    # ALTERNATE SOLUTION:

    # if len(a) == 0:
    #     return b
    # if len(b) == 0:
    #     return a

    # combined_lists_sorted = []
    # ai = 0  # Index of a list
    # bi = 0  # Index of b list

    # while ai < len(a) or bi < len(b):
    #     if ai == len(a):
    #         combined_lists_sorted.append(b[bi])
    #         bi += 1
    #         continue
    #     if bi == len(b):
    #         combined_lists_sorted.append(a[ai])
    #         ai += 1
    #         continue
    #     if a[ai] <= b[bi]:
    #         combined_lists_sorted.append(a[ai])
    #         ai += 1
    #     else:
    #         combined_lists_sorted.append(b[bi])
    #         bi += 1

    # return combined_lists_sorted


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"

"""Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    # if not haystack:
    #     return

    # current = haystack[0]

    # if current == needle:
    #     return 0
    # if not haystack[1:]:
    #     return 0
    # else:
    #     return 1 + recursive_index(needle, haystack[1:])

    def _recursive_index(needle, haystack, count):

        if count > (len(haystack) - 1):
            return

        if needle == haystack[count]:
            return count

        else:
            return _recursive_index(needle, haystack, count + 1)

    return _recursive_index(needle, haystack, 0)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO GO GO!\n"

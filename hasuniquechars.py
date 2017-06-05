"""Does word contains unique set of characters?

For example::

    >>> has_unique_chars("Monday")
    True

    >>> has_unique_chars("Moonday")
    False

    >>> has_unique_chars("")
    True

Uppercase and lowercase letters should be considered separately::

    >>> has_unique_chars("Bob")
    True
"""


def has_unique_chars(word):
    """Does word contains unique set of characters?"""

    chars_count = {}

    for char in word:
        char_count = chars_count.get(char)
        if char_count is not None:
            return False
        else:
            chars_count[char] = chars_count.get(char, 0) + 1

    return True

    # ALTERNATE SOLUTION:

    # return sorted(list(set(word))) == sorted(list(word))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME!\n"

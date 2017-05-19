"""Decode a string.

A valid code is a sequence of numbers and letter, always starting with a number
and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string "hey" could be encoded by "0h1ae2bcy". This means
"skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

A single letter should work::

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'
"""


def decode(s):
    """Decode a string."""

    # Initialize new string
    # Loop through given string
    # Keep track of index you're on
    # If encounter a number, add the letter that number of indices away to the initialized string
    # Return the initialized string

    decoded_string = ""
    i = 0

    while i < len(s):
        num = int(s[i])
        i += 1 + num
        char_to_add = s[i]
        decoded_string += char_to_add
        i += 1

    return decoded_string


    # ALTERNATE SOLUTION:
    # decoded_string = ""

    # for i in range(len(s)):
    #     char_to_check = s[i]
    #     if char_to_check in "0123456789":
    #         char_to_add = s[i + int(char_to_check) + 1]
    #         decoded_string += char_to_add

    # return decoded_string


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; 0G1ar0e1ba0t2ab! ***\n"

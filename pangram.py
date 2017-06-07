"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    used = {char.lower() for char in sentence if char.isalpha()}
    return len(used) == 26



    # ALTERNATE SOLUTION:

    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # alphabet_count = {}

    # for letter in alphabet:
    #     alphabet_count[letter] = 1

    # for char in sentence:
    #     if char not in "!.,? ":
    #         count = alphabet_count.get(char.lower())
    #         alphabet_count[char.lower()] = count - 1

    # return max(alphabet_count.values()) == 0



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"

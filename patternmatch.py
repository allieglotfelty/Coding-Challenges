"""Check if pattern matches.

Given a "pattern string" starting with "a" and including only "a" and "b"
characters, check to see if a provided string matches that pattern.

For example, the pattern "aaba" matches the string "foofoogofoo" but not
"foofoofoodog".

Patterns can only contain a and b and must start with a:

    >>> pattern_match("b", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

    >>> pattern_match("A", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

    >>> pattern_match("abc", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

The pattern can contain only a's:

    >>> pattern_match("a", "foo")
    True

    >>> pattern_match("aa", "foofoo")
    True

    >>> pattern_match("aa", "foobar")
    False

It's possible for a to be zero-length (a='', b='hi'):

    >>> pattern_match("abbab", "hihihi")
    True

Or b to be zero-length (a='foo', b=''):

    >>> pattern_match("aaba", "foofoofoo")
    True

Or even for a and b both to be zero-length (a='', b=''):

    >>> pattern_match("abab", "")
    True

But, more typically, both are non-zero length:

    >>> pattern_match("aa", "foodog")
    False

    >>> pattern_match("aaba" ,"foofoobarfoo")
    True

    >>> pattern_match("ababab", "foobarfoobarfoobar")
    True

Tricky: (a='foo', b='foobar'):

    >>> pattern_match("aba" ,"foofoobarfoo")
    True
"""

def is_a_match(pattern, a, b, astring):
    """Does astring match pattern using proposed values for a and b?"""

    test_string = ""

    for p in pattern:
        if p == "a":
            test_string += a
        else:
            test_string += b

    return test_string == astring

def pattern_match(pattern, astring):
    """Can we make this pattern match this string?"""
 
    # Q&D sanity check on pattern

    assert (pattern.replace("a", "").replace("b", "") == ""
        and pattern.startswith("a")), "invalid pattern"

    num_a = pattern.count("a")
    num_b = pattern.count("b")
    first_b = pattern.find("b")

    for a_length in range(0, len(astring) / num_a + 1):
        if num_b:
            b_length = (len(astring) - (a_length * num_a)) / float(num_b)
        else:
            b_length = 0

        if int(b_length) != b_length or b_length < 0:
            continue

        b_start = first_b * a_length

        if is_a_match(pattern=pattern,
                      a=astring[0:a_length],
                      b=astring[b_start:b_start + int(b_length)],
                      astring=astring):
            return True

    return False 


# ALTERNATE SOLUTION:
# def pattern_match(pattern, astring):
#     """Can we make this pattern match this string?"""

#     # Q&D sanity check on pattern

#     assert (pattern.replace("a", "").replace("b", "") == ""
#             and pattern.startswith("a")), "invalid pattern"


#     if astring == "" or pattern == "a":
#         return True

#     pattern_length = len(pattern)
#     string_length = len(astring)

#     if not "b" in pattern:
#         if string_length % pattern_length != 0:
#             return False
#         diff = string_length / pattern_length
#         to_check = set()
#         i = 0
#         while i < string_length:
#             to_check.add(astring[i:i+diff])
#             i += diff
#         return len(to_check) == 1

#     return is_repeating_pattern(pattern, astring)



# def is_repeating_pattern(pattern, astring):
#     """Checks if the pattern is repeating, so the pattern includes an empty
#     string of 'a's or an empty string of 'b's.
#     """

#     pattern_length = len(pattern)
#     string_length = len(astring)

#     num_a = get_letter_count("a", pattern)
#     num_b = get_letter_count("b", pattern)


#     if string_length % num_b == 0:
#         diff = string_length / num_b
   
#     if string_length % num_a == 0:
#         diff = string_length / num_b

#     to_check = set()
#     i = 0

#     while i < string_length:
#         to_check.add(astring[i:i+diff])
#         i += diff

#     return len(to_check) == 1


def get_letter_count(letter, pattern):
    """Gets the number of times that letter appears in the pattern."""

    letter_count = 0

    for let in pattern:
        if let == letter:
            letter_count += 1

    return letter_count



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WE'RE WELL-MATCHED!\n"

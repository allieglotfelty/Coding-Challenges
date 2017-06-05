"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> find_mode([1]) == {1}
    True

    >>> find_mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> find_mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def find_mode(nums):
    """Find the most frequent num(s) in nums."""

    num_counts = {}

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    top_counts = set()

    max_count = max(num_counts.values())

    for k, v in num_counts.items():
        if v == max_count:
            top_counts.add(k)

    return top_counts



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"

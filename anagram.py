"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, as it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""

    d = {}

    for word in wordlist:
        letters = ''.join(sorted(list(word)))
        d[letters] = d.get(letters, []) + [word]

    most = None

    for k, v in d.items():
        if not most:
            most = (k, v)
        elif len(v) > len(most[1]):
            most = (k, v)

    return most[1][0]

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"

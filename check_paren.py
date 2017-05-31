"""
input #  output
'{}()' # True
'['  # False
']'  # False
'[()]' # True
'[)(]' # False
'[((())]' # False
'[(]' # False
    """

def check_parens(string):
    """Check if parentheses are balanced in the string.

    >>> check_parens('{}()')
    True

    >>> check_parens('[')
    False

    >>> check_parens(']')
    False

    >>> check_parens('[()]')
    True

    >>> check_parens('[)(]')
    False

    >>> check_parens('[((())]')
    False

    >>> check_parens('[(]')
    False
    """

    check_stack = []

    for p in string:
        if p in "{[(":
            check_stack.append(p)
        if p in "}])":
            if not check_stack:
                return False
            if p == ')' and check_stack[-1] == '(':
                check_stack.pop()
            elif p == ']' and check_stack[-1] == '[':
                check_stack.pop()
            elif p == '}' and check_stack[-1] == '{':
                check_stack.pop()
            else:
                continue

    return not check_stack

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT JOB! ****\n"
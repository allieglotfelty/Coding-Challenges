"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""

    values = s.split()

    num1 = int(values.pop())

    while values:
        num2 = int(values.pop())
        operator = values.pop()
        if operator == '-':
            num1 = num2 - num1
        elif operator == '+':
            num1 = num2 + num1
        elif operator == '*':
            num1 = num2 * num1
        elif operator == '/':
            num1 = num2 / num1

    return num1


    # ALTERNATE SOLUTION:

    # values = s.split()

    # expressions = []
    # nums = []

    # for v in values:
    #     if v in "-+*/":
    #         expressions.append(v)
    #     else:
    #         nums.append(v)

    # expression = ''
    # while expressions and nums:
    #     exp = expressions.pop(0)
    #     num = nums.pop(0)
    #     expression += '(' + num + exp
    # if len(values) > 3:
    #     expression += nums[0] + '))'
    # else:
    #     expression += nums[0] + ')'

    # return eval(expression)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n"

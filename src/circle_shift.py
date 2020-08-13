"""
   Left-Right Circle Shift
   @author Rafael
"""

#!/bin/python3


def getShiftedString(s, leftShifts, rightShifts):
    """
    Generate the string after the following operations
    1. Left Circle Shift 
    2. Right Circle Shift

    :type s: string
    :type leftShifts: int
    :type rightShifts: int

    Examples:
    >>> getShiftedString("abc",1,0)
    'bca'
    >>> getShiftedString("abc",1,7)
    'abc'
    """

    # Limit Huge Shifts
    sLen = len(s)
    leftShifts = leftShifts % sLen
    rightShifts = rightShifts % sLen

    # Generate Left shifted string
    leftS = s[leftShifts:] + s[:leftShifts]

    # Generate Right shifted string
    rightS = leftS[-rightShifts:] + leftS[0:-rightShifts]

    return rightS

if __name__ == '__main__':
    # Test Trivial Cases with doctest
    import doctest
    doctest.testmod()


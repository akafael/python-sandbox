"""
    lesson 1 - Binary Gap Problem
    ref: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
    @author Akafael
"""

# !/usr/bin/env python

import unittest


def binary_str(num):
    """ Return a binary string representation from the posive interger 'num'
    :type num: int
    :return:

    Examples:
    >>> binary_str(2)
    '10'
    >>> binary_str(5)
    '101'
    """

    # Store mod 2 operations results as '0' and '1'
    bnum = ''
    while num > 0:
        bnum = str(num & 0x1) + bnum
        num = num >> 1

    return bnum


def binary_gap(num):
    """Return the count of the largest amount of zeros between ones in the binary representation of num
    :type num: int

    Examples:
    >>> binary_gap(9)
    2
    >>> binary_gap(529)
    4
    >>> binary_gap(20)
    1
    >>> binary_gap(3)
    0
    """

    gap_size = 0
    larger_gap = 0

    class FSMStates:
        START = 0
        COUNT = 1
        IDLE = 2

    # Count '0' sequence length
    state = FSMStates.IDLE
    while num > 0:
        # Get Each Binary Digit
        digit = num & 0x1
        num = num >> 1

        # Check State
        if digit == 0x1:
            # Change State
            state = FSMStates.START
        elif digit == 0x0:
            if state != FSMStates.IDLE:
                state = FSMStates.COUNT

        # Run State Action
        if state == FSMStates.START:
            # Store Longest 0 sequence
            if gap_size > larger_gap:
                larger_gap = gap_size
            # Reset Counter
            gap_size = 0
        elif state == FSMStates.COUNT:
            # Increment Counter
            gap_size += 1

    return larger_gap


class TestBinaryGap(unittest.TestCase):

    def test_prop_maxvalue(self):
        """
        Number Should be less then binary digit representation size
        :return: null
        """
        num = 10
        self.assertGreaterEqual(num // 2, binary_gap(num))
        self.assertGreaterEqual(len(binary_str(num)), binary_gap(num))


if __name__ == '__main__':
    # Test Trivial Cases with doctest
    import doctest
    doctest.testmod()

    # Unit Tests
    unittest.main()


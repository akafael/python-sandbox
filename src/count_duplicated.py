"""
   Count duplicated numbers in a list
   @author Rafael
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def countDuplicate(numbers):
    """
    Count Duplicated Number in a list
    :type numbers: interger_array
    :return: interger

    Examples:
    >> countDuplicated([1,2,1,2,3,4,4])
    3
    >> countDuplicated([1,2,3,4])
    0
    """

    count = 0;
    dCount = {}

    # Detect Non Unique Numbers
    for n in numbers:
        if n in dCount:
            dCount[n] += 1

            # Count First Duplicated time for this number
            if dCount[n] == 2:
                count += 1
        else:
            dCount[n] = 1

    return count
    

if __name__ == '__main__':
    # Test Trivial Cases with doctest
    import doctest
    doctest.testmod()


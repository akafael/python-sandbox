"""
   Check Palidromes
   @author Akafael
"""

#!/bin/python3

def is_palidrome_oneline(word):
    """
    Check if word is palidrome using buildin python functions
    :type word: string
    :return: bool

    Examples:
    >> is_palidrome_oneline("aaabbaaa")
    True
    >> is_palidrome_oneline("banana")
    False
    """
    return False not in set([inputString[i]==inputString[-i-1] for i in range(len(inputString))])


if __name__ == '__main__':
    # Test Trivial Cases with doctest
    import doctest
    doctest.testmod()


"""
Bubble Sort Algorithm
 @complexity O(n^2)
 @author Akafael
 @ref https://en.wikipedia.org/wiki/Bubble_sort
"""


# !/usr/bin/env python


def bubble_sort(arr):
    """ Sort Array Elements using Bubble Sort Algorithm
    :return:

    Examples:
    >>> bubble_sort([1])
    [1]
    >>> bubble_sort([10,9,8,7,6,5,4,3,2,1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """

    # Traverse through all array elements
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place 
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    # Test Trivial Cases with doctest
    import doctest
    doctest.testmod()


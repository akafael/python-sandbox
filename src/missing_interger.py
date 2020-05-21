"""
Find the smallest missing int greater then 1 in array
 @complexity O(n^2)
 @author Rafael
"""


def missing_interger(A):
    """
    Find the smallest missing int greater then 1 in array
    """
    n = len(A)

    A.sort()

    # Find First Max
    missing_int = 1
    for i in range(n):
        if A[i] < 0:
            pass
        elif A[i] == missing_int:
            missing_int = A[i] + 1

    return missing_int

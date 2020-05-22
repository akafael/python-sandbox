"""
Find local max and min
 @author Akafael
"""

def count_local_minmax(A):
    """
    Count local max and min
     @author Akafael
    """

    n = len(A)

    # Trivial Solution
    if n <= 1:
        return 1

    # Calculate the diff
    B = []
    count = 0
    isRising = False
    isFalling = False
    for i in range(1, n - 1):
        B.append(A[i + 1] - A[i])

        # Count Pikes
        if B[i] > 0:
            isRising = True
            if isFalling == True:
                count += 1
                isFalling == False
        elif B[i] < 0:
            isFalling = True
            if isRising == True:
                count += 1
                isRising == False

    return count

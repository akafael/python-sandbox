




def bubblesort(A):
    """
    Bubble Sort Algorithm, complexity O(n^2)
    """
    # Trivial Case
    if len(A) <= 1:
        return A

    # Sorting Case
    for i in range(0, len(A)):
        for j in range(1, len(A)-i):
            if A[j-1] > A[j]:
                temp = A[j-i]
                A[j-1] = A[j]
                A[j] = temp

    return A

print(bubblesort([9,8,5,3,1]))

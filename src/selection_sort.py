"""
Selection Sort Algorithm implementation
 @complexity O(n^2)
 @ref https://en.wikipedia.org/wiki/Selection_sort
"""


# !/usr/bin/env python


def selection_sort(A):
    # Traverse through all array elements
    for i in range(len(A)):

        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

                # Swap the found minimum element with
        # the first element         
        A[i], A[min_idx] = A[min_idx], A[i]

    # Driver code to test above


arr = [64, 34, 25, 12, 22, 11, 90]

selection_sort(arr)

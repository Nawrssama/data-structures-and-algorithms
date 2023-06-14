def Mergesort(arr):
    """
    Sorts a list of integers in ascending order using the merge sort algorithm.

    Parameters:
        arr (list): List of integers to be sorted.

    Returns:
        list: Sorted list of integers.
    """
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        # sort the left side 
        Mergesort(left)
        # sort the right side 
        Mergesort(right)
        # merge the sorted left and right sides togetther
        Merge(left , right , arr)
    return arr

def Merge(left , right , arr):
    """
    Merges two sorted lists into a single sorted list.

    Parameters:
        left (list): Sorted list of integers.
        right (list): Sorted list of integers.
        arr (list): List to store the merged result.

    Returns:
        list: Merged and sorted list of integers.
    """
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else :
            arr[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        arr[k:] = right[j:]
    else:
        arr[k:] = left[i:]

print(Mergesort([8,5,7,3,4,9,1]))

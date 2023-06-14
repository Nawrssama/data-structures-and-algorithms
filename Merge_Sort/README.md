# Marge Sort

> create a method that sorts a function based on the input array

# Approach & Efficiency

> Time ==> O(n log n)

> space ==> O(n)

# white-board

## Marge Sort
![Marge Sort ](./Marge%20Sort.jpg)


# Solution 

    def Mergesort(arr):
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
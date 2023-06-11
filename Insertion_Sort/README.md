# Insertion Sort

> create a method that sorts a function based on the input array

# Approach & Efficiency

> Time ==> O(n^2)

> space ==> O(n)

# white-board

## Insertion Sort
![Insertion Sort ](./Insertion%20Sort.jpg)


# Solution 

    def insert(sorted , int):
        i = 0
        while i < len(sorted) and int > sorted[i]:
            i += 1
        while i < len(sorted):
            temp = sorted[i]
            sorted[i] = int
            int = temp
            i += 1
        sorted.append(int)

    def insert_sort (input):
        sorted = []
        sorted.append(input[0])
        for i in range(1 , len(input)):
            insert(sorted , input[i])
        return sorted
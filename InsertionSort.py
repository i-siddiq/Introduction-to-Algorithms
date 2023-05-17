# Insertion Sort Example.
# Efficient Algorithm for sorting a small number of elements

def InsertionSort(A,n):
    for i in range(1,n):
        key = A[i]
        j = i - 1
        while j>-1 and A[j]> key:
            A[j + 1] = A[j]
            j = j - 1
            A[j + 1] = key

    print(A)

Array = [5,2,4,6,1,3]
InsertionSort(Array,6)

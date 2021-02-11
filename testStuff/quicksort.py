#Quicksort Lomuto Partition Scheme
import random
unsorted = [random.randint(0, 100) for _ in range(10)]

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo, hi):
        if A[j] < pivot:
            a = A[i]
            A[i] = A[j]
            A[j] = a
            i += 1
    a = A[hi]
    A[hi] = A[i]
    A[i] = a
    return i

quicksort(unsorted, 0, len(unsorted) - 1)
print(unsorted)
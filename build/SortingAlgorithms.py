#Sorting Algorithms
#Example array A
A = [2, 3, 1, 0, 4, 4, 2, 0, 9, 1, 0, 9, 8, 7, 6]
print("-----------------------------------------------------------")
print("-------" + str(A) + "-------")
print("-----------------------------------------------------------")

#--------------------insertion_sort--------------------
def insertion_sort(A):
    for i in range(len(A)):
        dummy = A[i]
        j = i
        while (j > 0 and A[j-1] > dummy):
            A[j] = A[j-1]
            j = j - 1

        A[j] = dummy
    return A


#--------------------bubble_sort--------------------
def bubble_sort(A):
    for i in range(len(A), 1, -1):
        for j in range(1, i-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A


#--------------------merge_sort--------------------
def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


# --------------------quick_sort--------------------
import random

def quick_sort(A):
    if len(A) <= 1:
        return A
    else:
        pivot = random.choice(A)
        left = [x for x in A if x < pivot]
        middle = [x for x in A if x == pivot]
        right = [x for x in A if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

print()
print("insertion_sort: " + str(insertion_sort(A)))
print("bubble_sort: " + str(bubble_sort(A)))
print("merge_sort: " + str(merge_sort(A)))
print("quick_sort: " + str(quick_sort(A)))

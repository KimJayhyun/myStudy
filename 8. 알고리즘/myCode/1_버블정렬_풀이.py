from typing import MutableSequence

def bubblesort_desc(a : MutableSequence):
    swap = True
    length = len(a)

    for i in range(length - 1):
        for j in range(length - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]        
                swap = True
        if not swap:
            break

def bubblesort_asc(a : MutableSequence):
    swap = True
    length = len(a)

    for i in range(length - 1):
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]        
                swap = True
        if not swap:
            break


arr = [1, 9, 3, 2]
bubblesort_desc(arr)
print(arr)
bubblesort_asc(arr)
print(arr)

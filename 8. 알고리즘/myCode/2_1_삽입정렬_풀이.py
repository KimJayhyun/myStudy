from typing import MutableSequence
import random

def insertionSort(arr : MutableSequence):
    length = len(arr)

    for i in range(1, length):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] =  arr[j - 1], arr[j]
            else :
                break

data_list = random.sample(range(100), 50)
insertionSort(data_list)
print(data_list)

import time
from random import *


def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    # a = [4, 1, 6, 2, 88, 3, 24, 53]
    a = [randrange(1000000) for i in range(1000000)]
    start = time.time()
    print(bubbleSort(a))
    end = time.time()
    print(end-start)

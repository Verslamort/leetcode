import time
from random import randrange


def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2), -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        arrLen -= 1
        heapify(arr, 0)
    return arr


if __name__ == '__main__':
    # a = [10, 13, 20, 21, 30, 35, 46, 60, 65, 77, 81, 91, 96]
    # print(heapSort(a))
    a = [randrange(1000000) for i in range(1000000)]
    start = time.time()
    print(heapSort(a))
    end = time.time()
    print(end - start)


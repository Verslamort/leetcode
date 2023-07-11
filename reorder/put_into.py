from random import randrange
import time


def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr


if __name__ == '__main__':
    a = [randrange(1000000) for i in range(1000000)]
    start = time.time()
    print(insertionSort(a))
    end = time.time()
    print(end - start)

import time
from random import randrange


def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


if __name__ == '__main__':
    # a = [4, 1, 6, 2, 88, 3, 24, 53]
    # print(selectionSort(a))
    a = [randrange(1000000) for i in range(1000000)]
    start = time.time()
    print(selectionSort(a))
    end = time.time()
    print(end - start)

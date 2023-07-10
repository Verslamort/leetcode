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
    a = [4, 1, 6, 2, 88, 3, 24, 53]
    print(insertionSort(a))

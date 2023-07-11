# 数组相对排序
"""
给定两个数组，arr1 和arr2，
arr2中的元素各不相同
arr2 中的每个元素都出现在arr1中
对 arr1中的元素进行排序，使 arr1 中项的相对顺序和arr2中的相对顺序相同。未在arr2中出现过的元素需要按照升序放在arr1的末尾。
"""


def sort(arr1, arr2):
    a = []
    for i in arr1:
        if i not in arr2:
            a.append(i)
            a.sort()
            arr1 = arr2 + a
    return arr1


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(sort(arr1, arr2))

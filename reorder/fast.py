# 快速排序
def quickSort(alist, start, end):
    if start >= end:  # 递归退出条件
        return
    mid = alist[start]  # 设置起始基准元素
    low = start  # low为序列左边在开始位置由左向右的游标
    high = end  # high为右边末尾位置的由右向左的游标
    while low < high:
        # 如果low与high没有重合，high（右边）指向的元素大于等于基准元素，则high向左移
        while low < high and alist[high] >= mid:
            high -= 1
        # 此位置high指向一个比基准元素小的元素，将high指向的元素放到low的位置上，此时high指向的位置为空，移动low找到符合条件的元素放在此处
        alist[low] = alist[high]
        # 如果low与high没有重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 此时low指向一个比基准元素大的元素，将low指向的元素放到high空着的位置上，low指向位置变空，循环，将high找的符合条件的元素放到此处
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置，左边元素比基准小，右边元素比基准大
    alist[low] = mid  # 基准元素放到该位置
    # 对基准元素左边的子序列进行快速排序
    quickSort(alist, start, low-1)
    quickSort(alist, low+1, end)


if __name__ == '__main__':
    a = [4, 1, 6, 2, 88, 3, 24, 53]
    quickSort(a, 0, len(a)-1)
    print(a)

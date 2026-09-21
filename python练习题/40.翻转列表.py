def reverse(list1, length):
    print(f"交换前：{list1}")
    m = 0
    n = length - 1
    while True:
        if (m < n):
            list1[m],list1[n] = list1[n],list1[m]
            m += 1
            n -= 1
        else:
            break
    print(f"交换后：{list1}")
list1 = [10, 11, 12, 13, 14, 15]
n = len(list1)
reverse(list1, n)
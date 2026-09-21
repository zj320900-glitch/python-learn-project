#使用队列
def reverse(arr, d, n):
    from collections import deque
    print(f"翻转前的数组为：{arr}")
    temp = deque()
    for i in range(0, n):
        temp.append(arr[i])
    #temp = deque(arr)
    print(temp)
    for i in range(0, d):
        number = temp.popleft()
        temp.append(number)
    print(temp)
    for i in range(0, n):
        arr[i] = temp[i]
    print(f"翻转后的数组为：{arr}")
arr = [1, 2, 3, 4, 5, 6, 7]

reverse(arr, d=2, n=len(arr))
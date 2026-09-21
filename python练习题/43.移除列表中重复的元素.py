#使用列表推导式
def guolv(list1):
    unique_list = []
    print("去重前：", list1)
    [unique_list.append(item) for item in list1 if item not in unique_list]
    print("去重后：", unique_list)
original_list = [1, 2, 2, 3, 4, 4, 5]
guolv(original_list)
#使用队列
from collections import deque
def guolv2(list1, n):
    print("去重前：", list1)
    temp = deque(list1)
    new_deque = deque()
    print(temp)
    for _ in range(n):
        elemnt = temp.popleft()
        if elemnt not in new_deque:
            new_deque.append(elemnt)
    print("去重后：",list(new_deque))
original_list = [1, 2, 2, 3, 4, 4, 5, 5]
length = len(original_list)
guolv2(original_list, length)

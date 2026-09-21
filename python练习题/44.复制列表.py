def clone_runoob(li1):
    li_copy = list(li1)
    return li_copy
li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)
print("原始列表:", li1)
print("复制后列表:", li2)
def clone_runoob1(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy
li3 = [4, 8, 2, 10, 15, 18]
li4 = clone_runoob1(li3)
print("原始列表:", li3)
print("复制后列表:", li4)
def clone_runoob2(li1):
    li_copy = li1[:]
    return li_copy
li5 = [4, 8, 2, 10, 15, 18]
li6 = clone_runoob(li5)
print("原始列表:", li5)
print("复制后列表:", li6)
print()
#使用队列
def clone_runoob3(list1, n):
    print("原始列表:", list1)
    from collections import deque
    temp_deque = deque(list1)
    new_deque = deque()
    for _ in range(n):
        temp_element = temp_deque.popleft()
        new_deque.append(temp_element)
    print("复制后列表：", list(new_deque))
li7 = [4, 8, 2, 10, 15, 18]
length = len(li7)
clone_runoob3(li7, length)
  
    


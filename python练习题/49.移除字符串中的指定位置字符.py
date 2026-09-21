def remove_str(str1, pos, length):
    list_temp = list(str1)
    print(list_temp)
    from collections import deque
    temp_deque = deque(list_temp)
    print(temp_deque)
    temp = 1
    for _ in range(length):
        temp_str = temp_deque.popleft()
        if (temp == pos):
            temp += 1
            continue
        else:
            temp_deque.append(temp_str)
        temp += 1
    list_new = list(temp_deque)
    for i in list_new:
        print(f"{i}", end="")
str1 = list("runoob")
pos = 3
length = len(str1)
remove_str(str1, pos, length)



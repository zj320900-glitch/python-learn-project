RUNOOB = [6, 0, 4, 1]
print("清空前：", RUNOOB)
RUNOOB.clear()
print("清空后：", RUNOOB)


from collections import deque
temp = deque({1, 2, 3})
print(temp)
print(3 in temp)
print(3 not in temp)

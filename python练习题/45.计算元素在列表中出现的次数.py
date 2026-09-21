def number_count(list1, x):
    count = 0 
    for i in list1:
        if (i == x):
            count += 1
    return count
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10, 10, 10]
x = 10
result = number_count(lst, x)
print(f"元素 {x} 在列表lst中出现的次数为：{result}")

def countX(lst, x):
    return lst.count(x)
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))

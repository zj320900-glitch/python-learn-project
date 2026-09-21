def sum_number(list1):
    sum = 0 
    for i in list1:
        sum += i
    return sum
list1 = [11, 5, 17, 18, 23] 
result = sum_number(list1)
print(f"列表{list1}的元素之和为：{result}")

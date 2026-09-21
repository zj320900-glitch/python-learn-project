def mulity(list1):
    chengji = 1
    for i in list1:
        chengji *= i
    return chengji
list1 = [1, 2, 3, 4]
result = mulity(list1)
print(f"列表{list1}的元素乘积为：{result}")
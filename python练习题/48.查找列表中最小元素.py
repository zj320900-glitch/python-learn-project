def search_lowest(list1):
    min_element = list1[0]
    for i in list1:
        if (min_element > i):
            min_element = i
    return min_element
list1 = [10, 20, 4, 0, -1]
result = search_lowest(list1)
print(f"列表{list1}的最小元素为：{result}")
print(min(list1))
print(max(list1))



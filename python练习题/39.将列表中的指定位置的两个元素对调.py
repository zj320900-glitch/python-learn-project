def exchange_element(list1, pos1, pos2):
    print(f"交换前：{list1}")
    temp = list1[pos1-1]
    list1[pos1-1] = list1[pos2-1]
    list1[pos2-1] = temp
    print(f"交换后：{list1}")
def exchange_element1(list1, pos1, pos2):
    print(f"交换前：{list1}")
    get = list1[pos2-1],list1[pos1-1]
    list1[pos1-1],list1[pos2-1] = get
    print(f"交换后：{list1}")
def exchange_element3(list1, pos1, pos2):
    print(f"交换前：{list1}")
    list1[pos1-1],list1[pos2-1] = list1[pos2-1],list1[pos1-1]
    print(f"交换后：{list1}")
list1 = [1, 2, 3, 4, 5, 6]
exchange_element(list1, 2, 4)
exchange_element1(list1, 2, 4)
exchange_element3(list1, 2, 4)

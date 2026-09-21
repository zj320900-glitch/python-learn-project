def exchange(list1, n):
    print(f"交换前的列表为：{list1}")
    temp = list1[0] 
    list1[0] = list1[n-1]
    list1[n-1] = temp
    print(f"交换后的列表为：{list1}")
def exchange2(list1, n):
    print(f"交换前的列表为：{list1}")
    list1[0],list1[-1] = list1[-1],list1[0]
    
    print(f"交换后的列表为：{list1}")
list1 = [1, 2, 3]
n = len(list1)
exchange(list1, n)
exchange2(list1, n)

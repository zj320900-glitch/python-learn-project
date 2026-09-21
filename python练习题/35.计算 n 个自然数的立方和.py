def number_sum(n):
    sum = 0
    try:
        n = int(n)
        for i in range(1, n+1):
            sum = sum + (i ** 3)
        else:
            print(f"{n} 个自然数的立方和为：{sum}")
    except ValueError:
        print("您输入的不是数字，请重新输入！！！")
        return 1

while True:
    n = input("请输入您要计算的立方和数字：")
    temp = number_sum(n)
    if temp != 1:
        break 
def add(x, y):
    return x + y
def delease(x, y):
    return x - y
def multy(x, y):
    return x * y
def chu(x, y):
    return x / y
while True:
    print("请输入你要计算的两个数：")
    while True:
        try:
            m = int(input("请输入第一个数："))
            n = int(input("请输入第二个数："))
            break
        except ValueError:
            print("你输入的数据非法！")

    while True:
        print("输入1选择加法")
        print("输入2选择减法")
        print("输入3选择乘法")
        print("输入4选择除法")
        print("输入5选择退出")
        try:
            choice = int(input("请输入你要选择的计算方法："))
            break
        except ValueError:
            print("您输入了错误的方法，请重新输入!!!")
    if (choice == 1):
        print(f"{m} + {n} 的值为：{add(m, n)}")
        print()
    elif (choice == 2):
        print(f"{m} - {n} 的值为：{delease(m, n)}")
        print()
    elif (choice == 3):
        print(f"{m} * {n} 的值为：{multy(m, n)}")
        print()
    elif (choice == 4):
        print(f"{m} / {n} 的值为：{chu(m, n)}")
        print()
    else:
        print("即将退出！！！")
        break
        


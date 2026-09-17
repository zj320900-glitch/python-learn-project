def result_jiecheng(number):
    storage = number
    if (number == 0):
        print(f"{number} 的阶乘等于1")
    else:
        temp = 1
        while (number > 0):
            temp = temp * number
            number = number - 1
        else:
            print(f"{storage}! = {temp}")
number = int(input("请输入一个自然数："))
result_jiecheng(number)


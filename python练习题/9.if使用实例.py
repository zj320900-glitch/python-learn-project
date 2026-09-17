def check_number(a):
    try:
        b = float(a)
    except ValueError:
        print ("输入的不是数字！")
        return
    if b > 0:
        print(f"{b} 是正数")
    elif b < 0:
        print(f"{b} 是负数")
    else:
        print(f"{b} 等于0")
a = input("请输入你要判断的数字，并以enter键结束：")
check_number(a)


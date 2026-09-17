def change_number (a, b):
    print (f"交换前a的值为：{a}")
    print (f"交换前b的值为：{b}")
    c = a
    a = b
    b = c
    print (f"交换后a的值为：{a}")
    print (f"交换前b的值为：{b}")
def change_number1 (a, b):
    print (f"交换前a的值为：{a}")
    print (f"交换前b的值为：{b}")
    a, b = b, a
    print (f"交换后a的值为：{a}")
    print (f"交换后b的值为：{b}")

a = float(input("请输入a地值，并以enter键结束："))
b = float(input("请输入b地值，并以enter键结束："))
change_number(a, b)
change_number1(a, b)

c = input("1:")
float(c)
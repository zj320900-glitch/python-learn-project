def jisiuanmianji(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
    print (f"你输入的三角形面积为：{area}")
    print ("三角形")
a = float(input("输入三角形的第一条边，并以enter键结束："))
b = float(input("输入三角形的第二条边，并以enter键结束："))
c = float(input("输入三角形的第三条边，并以enter键结束："))
jisiuanmianji(a, b ,c)
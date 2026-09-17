def second_function(a, b ,c):
    print (f"您将要计算的二次方程为：{a}x**2 + {b}x + {c} = 0")
    result = (b**2) - 4*a*c
    if (result > 0):
        print ("该二次方程有两个实数根")
    elif (result < 0):
        print ("该方程没有实数根，但有两个复数根")
    else:
        print ("该方程有一个实数根")
    

print ("下面请输入三个实数来构造一个二次方程：")
a = float(input("请输入a的值，并以enter键结束："))
b = float(input("请输入b的值，并以enter键结束："))
c = float(input("请输入c的值，并以enter键结束："))
second_function(a, b ,c)
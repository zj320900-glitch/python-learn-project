num = float(input("请输入一个数字，并以enter键结束："))
num_sqrt = num ** 0.5
print (f"{num}的平方根为：", num_sqrt)
print (" %0.3f 的平方根为 %0.3f "%(num, num_sqrt))
print ("-------")
#负数的平方根
import cmath 
num1 = int(input("请输入一个数字："))
num_sqrt1 = cmath.sqrt(num1)
print (f"{num1}的平方根为：{num_sqrt1}")
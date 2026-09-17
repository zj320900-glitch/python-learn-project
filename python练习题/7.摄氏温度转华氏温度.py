def changedgree (degree):
    huasidegree = (degree * 1.8) + 32
    print (f"{degree} 转华氏温度的值为：{huasidegree}")
degree = float(input("请输入一个温度值，并以enter键结束："))
changedgree(degree)
def area (r):
    s = 3.14 * r * r
    print (f"圆的面积为：{s}")
r = float(input("请输入圆的边长，并以enter键结束："))
area(r)

import math
def calculate_circle_area(radius):
    return math.pi * radius **2
radius = 5
area = calculate_circle_area(radius)
print (f"半径为 {radius} 的圆的面积是 {area}")

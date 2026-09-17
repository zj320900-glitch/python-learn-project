year = int(input("输入一个年份："))
if (year % 4 == 0):
    if (year % 100 ==0):
        if (year % 400 ==0):
            print(f"{year} 年是闰年")
        else:
            print(f"{year} 年不是闰年")
    else:
        print(f"{year} 年是闰年")
else:
    print(f"{year} 年不是闰年")
#方式二
if (year % 4 ==0 and year %100 != 0) or (year % 400 == 0):
    print(f"{year} 年是闰年")
else:
    print(f"{year} 年不是闰年")
    

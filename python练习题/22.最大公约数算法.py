def result(m, n):
    max = 0
    
    for i in range(1, (min(n, m) + 1)):
        if ((n % i == 0) and (m % i == 0)):
            if (max < i):
                max = i
    else:
        print(f"{m} 和 {n} 的最大公约数为 {max}")


m = int(input("请输入数字m："))
n = int(input("请输入数字n："))
result(m, n)


def min_number(m, n):
    max = 0
    for i in range(1, (min(n, m) + 1)):
        if (n % i == 0) and (m % i == 0):
            if (max < i):
                max = i
    else:
        print(f"{m} 和 {n} 的最小公倍数为：{int((m * n) / max)}")

m = int(input("请输入数字m："))
n = int(input("请输入数字n："))

min_number(m, n)

def min_number2(m, n):
    greater = max(m, n)
    min = 0
    while True:
        if (greater % m == 0) and (greater % n ==0):
            if (min < greater):
                min = greater
                break
        greater = greater + 1

    print(f"{m} 和 {n} 的最小公倍数为 {min}")
                
                   
m = int(input("请输入数字m："))
n = int(input("请输入数字n："))

min_number2(m, n)
def sentence_zhishu(number):
    for n in range(2, number):
        if (number % n == 0 ):
            print(f"{number} = {n} * {number//n}，{number} 不是质数")
            break
        elif (n+1 == number):
            print(f"{number} 是质数")
number = int(input("请输入一个自然数："))
sentence_zhishu(number) 
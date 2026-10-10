#2026-09-16
def sentence_number(number, length):
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** length)
        temp = temp // 10
    else:
        if (sum == number):
            print(f"{number} 是阿姆斯特朗数")
        else:
            print(f"{number} 不是阿姆斯特朗数")

number = int(input("请输入一个数："))
length = len(str(number))
sentence_number(number, length)       


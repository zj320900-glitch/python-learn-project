def sentence_shushu(n, m):
    for i in range(n, m+1):
        for a in range(2, i):
            if (i % a == 0):
                print(f"{i} = {a} * {i // a}, {i} 不是素数")
                #if (i == (a + 1)):
                 #   print(f"{i} 是素数")
                #else:
                break
        else:
            print(f"{i} 是素数")
n = int(input("请输入你要判断的下限："))
m = int(input("请输入你要判断的上限："))
sentence_shushu(n, m)
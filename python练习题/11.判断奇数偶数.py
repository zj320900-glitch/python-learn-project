def sentence_number():
    while True:
        a = input("请输入：")
        try:
            float(a)
            if (float(a) % 2 == 0):
                print(f"{a}是偶数")
                break
            else:
                print(f"{a}不是偶数")
                break
        except ValueError:
            print("您输入的不是数字，请重新输入")

sentence_number()

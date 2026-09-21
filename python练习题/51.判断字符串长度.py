def str_length(str1):
    temp_list = list(str1)
    number = 0
    for i in temp_list:
        number += 1
    return number
str1 = "runoob"
result = str_length(str1)
print(f"字符串 {str1} 的长度为：{result}")

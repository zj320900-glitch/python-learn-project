def reverse(str1, length):
    n = 0
    m = length - 1
    
    while True:
        if(n < m):
            str1[n],str1[m] = str1[m],str1[n]
            n += 1
            m -= 1
        else:
            break
    print("1")
    print(''.join(str1))
str1 = list(str("runoobq"))
length = len(str1)
reverse(str1, length)
str = "Runoob"
print(str[::-1])
str = "Runoob"
print(''.join(reversed(str)))
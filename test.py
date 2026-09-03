print ("test")
print ("123")
def is_valid_identifier(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False

print(is_valid_identifier("2var"))  # False
print(is_valid_identifier("var2"))  # True

str="123456789"
print(str)
print(str[0:-1])  #最后一个数字不生效
print(str[0])
print(str[2:5])
print(str[2:])
print(str[1:6:2])
print(str*2)
print(str+'你好')
print('hello\nnihaoya')
print(r'hello\nnihaoya')
print('\n')
print(r'\n')
#input('\n\n按下enter键后退出\n')
import sys;x='runoob';sys.stdout.write(x+'\n')
x="a";y="b"
print(x)
print(y)
print(x,end="")
print(y,end="")
import sys
print("命令行参数为：")
for i in sys.argv:
    print(i)
print ("\n python路径为：",sys.path)
$ python -h 
#1.list定义
li = ["a", "b", "mpilgrim", "z", "example"]
print(li)
print(li[1])
print()
#2.list负数索引
print(li[-1])
print(li[-3])
print(li[1:3])
print(li[1:-1])
print(li[0:3])
print()
#3.list增加元素
print(li)
li.append("new")
print(li)
li.insert(2, "new")
print(li)
li.extend(["two", "elements"])
print(li)
print()
#list搜索
print(li)
print(li.index("example"))
print(li.index("new"))
try:
    print(li.index("c"))
except ValueError:
    print("c" in li)
print()
#list删除元素
print(li)
li.remove("z")
print(li)
li.remove("new")
print(li)
try:
    li.remove("c")
except:
    print("c" not in li)

print(li.pop())
print(li)
print()
li = ["a", "b", "mpilgrim"]
li = li + ["exampe", "new"]
print(li)
li += ["two"]
print(li)
li = [1, 2] * 3
print(li)
print()
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print([f"{k}={v}"  for k, v in params.items()])
print(";".join([f"{k}={v}" for k, v in params.items()]))
print()
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print(s)
print(s.split(";"))
print(s.split(";", 1))
print()
li = [1, 9, 8, 4]
print([elem*2 for elem in li])
print(li)
li = [elem*2 for elem in li]
print(li)
print()
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())
print([k for k, v in params.items()])
print([v for k, v in params.items()])
print([f"{k}={v}" for k, v in params.items()])
print()
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([elem for elem in li if len(elem) > 1])
print([elem for elem in li if elem != "b"])
print([elem for elem in li if li.count(elem) == 1])
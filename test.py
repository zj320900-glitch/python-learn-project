class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print (f"{self.name}说：我{self.age}岁。")
p = people("runoob", 10, 30)
p.speak()

class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        super().__init__(n, a, w)
        self.grade = g
    def speak(self):
        print (f"{self.name}说：我 {self.age} 岁了，我在读{self.grade}年级")

s = student("ken", 10, 60, 3)
s.speak()
class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print(f"我叫 {self.name}, 我是一个演说家，我演讲的主题是 {self.topic}")
class Sample(speaker, student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self,n, a, w, g)
        speaker.__init__(self, n, t)
test = Sample("Tim", 25, 80, 4, "Python")
test.speak()

print ("-------------")
class Parent:
    def myMethod(self):
        print ("调用父类方法")
class Child(Parent):
    def myMethod(self):
        #print ("调用子类方法")
        #super().myMethod()   #第一种调用父类方法
        Parent.myMethod(self)  #第二种调用父类方法
c = Child()
c.myMethod()
super(Child, c).myMethod()

print ("-----------")
class Father(object):
    def __init__(self, name):
        self.name = name
        print (f"name: {self.name}")
    def getName(self):
        return "Father" + self.name

class Son(Father):
    def getName(self):
        return "Son " + self.name

if __name__ == "__main__":
    son = Son("runoob")
    print (son.getName())

print ("------------")

class JustCounter:
    __secrestCount = 0
    publicCount = 0
    def count(self):
        self.__secrestCount += 1
        self.publicCount += 1
        print (self.__secrestCount)
counter = JustCounter()
counter.count()
print (counter.publicCount)
#print (counter.__secrestCount) #私有变量外部不能访问

print ("---------")
class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url
    def who(self):
        print ("name :", self.name)
        print ("url :", self.__url)
    def __foo(self):
        print ("这是私有方法")
    def foo(self):
        print ("这是公共方法")
        self.__foo()

x = Site ("菜鸟教程", "www.runoob.com")
x.who()
x.foo()
#x.__foo()  #会报错




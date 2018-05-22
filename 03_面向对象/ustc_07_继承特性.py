class Animal(object):
    # def __init__(self):
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


# 继承的传递性
class XiTianQ(Dog):
    def fly(self):
        print("飞")


A1 = Animal()
A1.run()

d1 = Dog()
d1.bark()
# 创造一个哮天犬类
X1 = XiTianQ()
X1.fly()

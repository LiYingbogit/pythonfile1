class Women:
    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s的年龄是%d" % (self.name, self.__age))

    def s1(self):
        self.__secret()


xiaofang = Women("小芳")
# 无法直接访问私有属性
# print(xiaofang.__age)
# xiaofang.secret()
# 在python中没有真正的私有，只有伪私有，但是不建议这样用，正常情况下，应尊重对象的私有属性，不去强行访问
xiaofang._Women__secret()
xiaofang.s1()

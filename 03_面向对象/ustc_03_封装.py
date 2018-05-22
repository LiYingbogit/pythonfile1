class Person:
    def __init__(self, name, weight):
        # self.属性=形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫[%s]体重是%s公斤" % (self.name, self.weight)

    def run(self):
        # pass
        print("%s爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        # pass
        print("%s爱吃东西，吃完东西再减肥" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaomei = Person("小美", 45.0)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
# print(xiaoming)

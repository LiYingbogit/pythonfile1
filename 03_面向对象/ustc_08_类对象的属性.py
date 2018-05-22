class Tool(object):
    # 使用赋值语句，定义类属性，记录创建类对象的总数
    count = 0

    def __init__(self, name):
        self.name = name
        # 针对类属性做一个加一操作
        Tool.count += 1


# 创建工具对象
t1 = Tool("锤子")
t2 = Tool("榔头")
# 属性的获取，存在一个向上查找机制
# 如果使用对象.类属性=值赋值语句，只会给对象添加一个属性，而不会影响到类属性的值
t2.count = 88
print(t2.count)
print(Tool.count)
print(t1.count)

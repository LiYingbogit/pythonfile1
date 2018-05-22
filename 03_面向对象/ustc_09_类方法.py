class Tool(object):
    count = 0

    # 类方法
    @classmethod
    def show_count(cls):
        print("工具对象总数:%d" % cls.count)

    # 实例方法
    def __init__(self, name):
        self.name = name
        Tool.count += 1

    # 静态方法 ,不需要访问类属性和实例属性
    @staticmethod
    def show():
        print("小狗快跑")


t1 = Tool("榔头")
Tool.show_count()
# 通过类名.调用静态方法，不需要创建对象
Tool.show()
print(Tool.count)

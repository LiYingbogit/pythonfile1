class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空
        if cls.instance is None:
            # 2.调用父类方法为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3.返回类属性对象保存的引用
        return cls.instance

    def __init__(self):

        # 1.判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 2.如果没有执行，执行初始化动作
        print("初始化播放器")
        # name1 = 0
        # 3.修改类属性标记
        MusicPlayer.init_flag = True


# 创建多个对象,单例模式的实际应用理解
player1 = MusicPlayer()
player1.name = 1
print(player1.name)

player2 = MusicPlayer()

print(player2.name)

print(player1)
print(player2)

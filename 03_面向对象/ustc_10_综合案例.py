class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("提示信息：放僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史最高分是%d" % cls.top_score)

    def start_game(self):
        print("%s开始游戏了。。。" % self.player_name)


# 1,提示信息
Game.show_help()
# 2.打印历史最高分
Game.show_top_score()
# 3.创建历史对象
xiaoming = Game("小明")
xiaoming.start_game()

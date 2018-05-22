class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count == 0:
            print("没有子弹了")
            return
        # 发射一颗子弹
        self.bullet_count -= 1

        print("%s 突突突 [%d]" % (self.model, self.bullet_count))


class Solider:
    def __init__(self, name):
        self.name = name
        self.gun = None


# 1.创建枪对象
AK47 = Gun("AK47")
AK47.add_bullet(50)
AK47.shoot()
# 2.创建一个士兵
xusanduo = Solider("许三多")
xusanduo.gun = AK47
print(xusanduo.gun)

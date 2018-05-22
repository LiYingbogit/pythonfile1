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

    def fire(self):
        # 1.判断士兵是否有枪
        # if self.gun == None:
        if self.gun is None:
            print("%s还没有枪" % self.name)
            return
        # 2.喊口号
        print("冲啊。。。%s" % self.name)
        # 3.加子弹
        self.gun.add_bullet(50)
        # 4.开枪
        self.gun.shoot()


# 1.创建枪对象
AK47 = Gun("AK47")

# 2.创建一个士兵
xusanduo = Solider("许三多")
xusanduo.gun = AK47
xusanduo.fire()
print(xusanduo.gun.model)

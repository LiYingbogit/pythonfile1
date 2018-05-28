import pygame

pygame.init()
# 创建游戏窗口大小 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图片
# 1>加载背景图片
bg = pygame.image.load("./images/background.png")
# 2>调用blit方法，绘制图像
screen.blit(bg, (0, 0))
# 3>调用update方法,更新屏幕显示
# pygame.display.update()

# 绘制英雄图片飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

# 可以在所有绘制工作都完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)
# 游戏循环
while True:
    # 指定循环体内部代码执行的频率，每秒执行60次
    clock.tick(60)
    # 捕获监听事件，pygame.event.get()返回是个列表
    event_list = pygame.event.get()
    # print(event_list)
    for event in event_list:
        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏结束")
            # 卸载所有模块
            pygame.quit()
            exit()
    # 2.修改飞机的位置
    hero_rect.y -= 1
    if (hero_rect.y + 126) <= 0:
        hero_rect.y = 700
    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))  # 绘制背景图像，这样只会看到最新飞机的图片
    screen.blit(hero, hero_rect)
    # 4.调用update方法更新显示
    pygame.display.update()
    # pass
pygame.quit()

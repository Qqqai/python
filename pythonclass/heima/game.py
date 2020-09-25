import pygame

# 初始化
pygame.init()

# 游戏代码
screen = pygame.display.set_mode((480, 700))
bg = pygame.image.load("./pythonclass\\heima\\images\\background.png")
screen.blit(bg, (0, 0))
pygame.display.update()

# 1> 加载图像
hero = pygame.image.load("./pythonclass\\heima\\images\\me1.png")

# 2> 绘制在屏幕
screen.blit(hero, (200, 500))

# 3> 更新显示
pygame.display.update()

# 3. 创建游戏时钟对象
clock = pygame.time.Clock()
i = 0

# 4. 定义英雄的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)

while True:

    # 设置屏幕刷新帧率
    clock.tick(60)

    # print(i)
    i += 1

    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)

    # 更新英雄位置
    # hero_rect.y -= 1

    # 如果移出屏幕，则将英雄的顶部移动到屏幕底部
    if hero_rect.y <= 0:
        hero_rect.y = 700

    # 绘制背景图片
    screen.blit(bg, (0, 0))
    # 绘制英雄图像
    screen.blit(hero, hero_rect)

    # 更新显示
    pygame.display.update()

    # 如果飞机超出屏幕了就让飞机从下面出来
    if hero_rect.bottom <= 0:
        hero_rect.top = 700
    elif hero_rect.left <= 0:
        hero_rect.left = 0
    elif hero_rect.bottom >= 700:
        hero_rect.bottom = 700
    elif hero_rect.right >= 480:
        hero_rect.right = 480

    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit...")
            exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print("left...")
                hero_rect.x -= 2
            if event.key == pygame.K_RIGHT:
                # print("right")
                hero_rect.x += 2
            if event.key == pygame.K_UP:
                hero_rect.y -= 2
            if event.key == pygame.K_DOWN:
                hero_rect.y += 2

# 游戏退出
pygame.quit()


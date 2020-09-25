from pythonclass.heima.plane.plane_constants import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

    def start_game(self):
        print("开始游戏...")
        while True:

            # 1. 设置刷新帧率
            self.clock.tick(PLANE_FPS)

            # 2. 事件监听
            self.__event_handler()

            # 3. 碰撞检测
            self.__check_collide()

            # 4. 更新精灵组
            self.__update_sprites()

    def __event_handler(self):
        """事件监听"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            # 5. 更新屏幕显示
            pygame.display.update()

    def __check_collide(self):
        """碰撞检测"""
        pass

    def __update_sprites(self):
        """更新精灵组"""
        pass

    def __create_sprites(self):
        """创建精灵组"""

        # 背景组
        self.back_group = pygame.sprite.Group()
        # 敌机组
        self.enemy_group = pygame.sprite.Group()
        # 英雄组
        self.hero_group = pygame.sprite.Group()

    def __update_sprites(self):
        """更新精灵组"""

        for group in [self.back_group, self.enemy_group, self.hero_group]:
            group.update()
            group.draw(self.screen)

    @staticmethod
    def __game_over():
        """游戏结束"""

        print("游戏结束")
        pygame.quit()
        exit(0)


# 入口
if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()

class Gun:
    """
    枪
    """

    def __init__(self, name):
        # 枪支名称
        self.name = name
        # 子弹数量
        self.bullet_count = 0

    # 添加子弹
    def add_bullet(self, count):
        self.bullet_count += count

    #射击!
    def shoot(self, count):
        if self.bullet_count <= 0:
            print("没有子弹，无法射击~")
            return
        if self.bullet_count <= count:
            print("子弹不足~  %s只能射击%d次~" % (self.name, self.bullet_count))
            return
        self.bullet_count -= count
        print("%s射击%d次，剩余%d颗子弹" % (self.name, count, self.bullet_count))


class Soldier:
    """
    士兵
    """

    def __init__(self, name):
        self.name = name
        # 假定士兵刚开始没有枪
        self.gun = None

    #开火！
    def fire(self, count):
        # 判断士兵是否有枪
        if self.gun is None:
            print("%s没有配发枪支~ 无法开火~" % self.name)
            return
        # 喊口号
        print("%s 冲啊" % self.name)
        # 开火
        self.gun.shoot(count)

    # 给士兵分配枪支
    def set_gun(self, gun):
        self.gun = gun
        print("%s得到了一把枪%s" % (self.name, gun.name))

    # 给枪装子弹
    def add_gun_bullet(self, count):
        # 判断士兵是否有枪
        if self.gun is None:
            print("%s没有配发枪支~ 无法装弹~" % self.name)
            return
        self.gun.add_bullet(count)


xu_san_duo = Soldier("许三多")
ak = Gun("ak47")
xu_san_duo.set_gun(ak)
xu_san_duo.add_gun_bullet(30)
xu_san_duo.fire(40)

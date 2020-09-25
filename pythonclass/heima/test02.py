# class Person:
#     """
#     人类
#     """

#     # 初始化
#     def __init__(self, name, weight):
#         self.weight = weight
#         self.name = name

#     def run(self):
#         self.weight = self.weight - 0.5
#         print("%s 在跑步,体重减到了%d" % (self.name, self.weight))

#     def eat(self):
#         self.weight += 1
#         print("%s 在吃东西，体重增加到了%d" % (self.name, self.weight))

#     def __str__(self):
#         return self.name + "体重" + str(self.weight)


# xiao_ming = Person("小明", 200)
# xiao_ming.run()
# xiao_ming.eat()
# print(xiao_ming)


class HouseItem:
    """
    家具类
    """

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return self.name + "占地：" + str(self.area) + "\n"


class House:
    """
    房子
    """

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        str1 = (
            "户型"
            + self.house_type
            + "\n"
            + "总面积:"
            + str(self.area)
            + "\n"
            + "剩余可用面积："
            + str(self.free_area)
            + "\n"
        )
        for item in self.item_list:
            str1 += str(item)
        return str1

    def add_item(self, house_item):
        # 判断剩余面积是否能够放得下当前家具
        if self.free_area < house_item.area:
            print("房间已经满了~")
            return
        self.item_list.append(house_item)
        self.free_area -= house_item.area


my_house = House("小三室", 100)
bed = HouseItem("西蒙斯", 20)
chest = HouseItem("衣柜", 15)
table = HouseItem("餐桌", 10)
my_house.add_item(table)
print(my_house)
my_house.add_item(chest)
print(my_house)
my_house.add_item(table)
print(my_house)

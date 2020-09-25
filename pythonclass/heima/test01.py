import random

# # 单价
# price = 8.5
# # 重量
# weigth = 7
# # 总价格
# AccmontPrice = price * weigth
# # 输出
# print(AccmontPrice)
# print(type(price))
# 输入
# a = input("第一个数")
# b = input("第二个数")
# print(int(a) + int(b))
# c = input()
# d = input()
# print(float(c) * float(d))
# print("名字:%s, 年龄:%d, 身高:%.2f" % (input("名字:"), int(input("年龄:")), float(input("身高:"))))

# if int(input("年龄:")) > 18:
#     print("允许进网吧")
# else:
#     print("不允许进网吧")

# if type(d) == int:
#     print("是整数")
# elif type(d) is s:
#     print("sing类型")


# def fun():
#     player = int(input("玩家出拳："))
#     if player is None:
#         fun()
#     computer_random_get = int(random.randint(1, 3))
#     if 1 == player:
#         if 2 == computer_random_get:
#             print("玩家赢")
#         elif 3 == computer_random_get:
#             print("电脑赢")
#         else:
#             print("平局")
#             fun()
#     elif 2 == player:
#         if 3 == computer_random_get:
#             print("玩家赢")
#         elif 1 == computer_random_get:
#             print("电脑赢")
#         else:
#             print("平局")
#             fun()
#     else:
#         if 1 == computer_random_get:
#             print("玩家赢")
#         elif 2 == computer_random_get:
#             print("电脑赢")
#         else:
#             print("平局")
#             fun()
# fun()

# i = 1
# while i <= 50:
#     print("hello python %s " % i)
#     i += 1
# print("结束")
# sum = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(sum)

# for i in range(0, 101, 2):
#     sum += i
# print(sum)

# 打印素数
# beign = int(input())
# end = int(input())
# prime_number = []
# if beign < 2:
#     for i in range(2, end, 1):
#         flag = True
#         for j in range(2, i + 1, 1):
#             if i % j == 0 and j != i:
#                 flag = False
#                 break
#         if flag:
#             prime_number.append(i)
# else:
#     for i in range(beign, end, 1):
#         flag = True
#         for j in range(beign, i + 1, 1):
#             if i % j == 0 and j != i:
#                 flag = False
#                 break
#         if flag:
#             prime_number.append(i)
# print(len(prime_number))


# three_seven_number = []
# for i in range(0, 100):
#     if i % 7 == 0 or i % 3 == 0:
#         three_seven_number.append(i)
# print(three_seven_number)

# end = 1
# j = 1
# while j <= 6 and j > 0:
#     print()
#     print("*" * j, end="")
#     if end == 1:
#         j += 1
#     else:
#         j -= 1
#     if j == 5:
#         end = 2

# row = int(input())
# i = 1
# while i <= row:
#     j = 1
#     while j <= i:
#         if i==j:
#             print("%d * %d = %d" % (j, i, i * j))
#         else:
#             print("%d * %d = %d" % (j, i, i * j), end="\t")
#         j += 1
#     i += 1

# 求两个传入数子的和，如果没有传入数字则默认两个数字都是1
# def add(a=1, b=1):
#     return a + b


# print(add(3, 4))
# print(add())

# 判断字符串是否是回文字符串
# def _is_back_s(s):
#     j = -1
#     s_1 = ""
#     s_2 = ""
#     for i in range(0, len(s), 1):
#         s_1 = s_1.__add__(s[i])
#         s_2 = s_2.__add__(s[j])
#         j = j.__add__(-1)
#     if s_1.__eq__(s_2):
#         return "true"
#     return "false"
# print(_is_back_s(input("输入字符串:")))


# def _ycbm_func(index, s):
#     count = 0
#     for i in range(0, index + 1, 1):
#         if i == 0:
#             count = 1
#             continue
#         if i == index:
#             if s[i - 1] == s[i - 2]:
#                 print("(%d,%s)" % (count, s[i - 1]), end="")
#                 break
#             else:
#                 print("(%d,%s)" % (1, s[i - 1]), end="")
#                 break
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             print("(%d,%s)" % (count, s[i - 1]), end=",")
#             count = 1
# s = input()
# _ycbm_func(len(s), s)

# sn = input()
# n = int(input())
# sum = 0
# for i in range(1, n + 1, 1):
#     sum = sum + int(i * sn)
# print(sum)


# def reserve(name_list, start, end):
#     while start < end:
#         # temp = list[start]
#         # list[start] = list[end]
#         # list[end] = temp
#         name_list[start], name_list[end] = name_list[end] name_list[start]
#         start += 1
#         end += 1


# name_list = ["张三"]
# name_list.append("王五")
# name_list.append("张三")
# print(name_list)
# reserve(name_list, 0, len(name_list))

# 求列表最大最小值
# def max_min_value(arr_list):
#     MAX_VALUE = 0
#     for x in arr_list:
#         if x > MAX_VALUE:
#             MAX_VALUE = x
#     MIN_VALUE = arr_list[0]
#     for s in arr_list:
#         if s < MIN_VALUE:
#             MIN_VALUE = s
#     return MAX_VALUE, MIN_VALUE

# value_list = [1,2,3,4,5,3,2424,342,53,45,34]
# a, b = max_min_value(value_list)
# print(a)
# print(b)

# 次大
# value_list = [1,2,3,4,5,3,2424,342,53,45,34]
# def find_scound_max_value(arr_list):
#     first_max = 0
#     scound_value = 0
#     for i in arr_list:
#         if i > first_max:
#             first_max = i
#         elif i > scound_value:
#             scound_value = i
#     return scound_value

# a = find_scound_max_value(value_list)
# print(a)

# dirc = {}
# dirc["name"] = "张三"
# dirc["age"] = 18
# dirc["sex"] = "女"
# print(dirc)
# for key, val in dirc.items():
#     print(key + ":" + str(val))

# input_str = input().strip()
# new_list = input_str.split(",")
# print("-".join(new_list))


# str = "abcdefghigklmn"
# print(str[2:6:1])
# print(str[2::1])
# print(str[::2])
# print(str[1::2])
# print(str[2::1])
# print(str[len(str) - 2::1])
# print(str[::-1])

# n = int(input())
# int_list = []
# for i in range(0, n, 1):
#     a, b = input("A、B:")
#     int_list.append(int(a))
#     int_list.append(int(b))
# print(int_list)


# value_list = [int(x) for x in input().strip().split(",")]
# print(value_list)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, x, y):
        print("eat..." + str(x + y))

    def run(self):
        print("run..." + self.name + str(self.age))


cat = Cat("张三", 18)
cat.eat(1, 2)
cat.run()


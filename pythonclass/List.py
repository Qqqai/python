#List.py
ls = input("in put a string:")
s = ls.split(",")
print("最大数：" + max(s))
print("最小数：" + min(s))
s = list(map(int, s))
count = sum(range(len(s) + 1))
print("加和：" + str(count))
print("平均数是：" + str(count / len(s)))
s.sort()
if len(s) % 2 == 0:
    print("中位数是：" + str( (s[len(s) / 2] + s[len(s) / 2 + 1]) / 2 ))
else:
    num = (len(s) - 1) / 2
    print("中位数是：" + str(s[int(num)]))
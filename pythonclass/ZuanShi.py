#ZuanShi.py
m = eval(input("m:"))
n = eval(input("n:"))
print("#" * m)
len = m - 2
for i in range(0, n+1, 1):
    print("#" + ("*" * i).center(len) + "#")
for i in range(n-1, -1, -1):
    print("#" + ("*" * i).center(len) + "#")
print("#" * m)
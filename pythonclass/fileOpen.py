# fileOpen.py
ft = open("paper.txt", "rt")
ft1 = open("paper1.txt", "wt")
ft2 = open("paper2.txt", "wt")
n = 0
for line in ft:
    n += 1
ft.seek(0)   
n1 = n // 2
n2 = n - n1
for i in range(n1):
    str = ft.readline()
    ft1.write(str)

for i in range(n2):
    str = ft.readline()
    ft2.write(str)
    
ft1.close()
ft2.close()
ft.close()

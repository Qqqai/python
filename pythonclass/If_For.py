#If_For.py

for i in range(7,1000,7):
    # if (i%2 == 0) and (i%3 == 2) and (i%4 == 3) and (i%5 == 4) and (i%6 ==5):
    #     print(i)
    #     break
    if (i%2 == 1) and (i%3 == 2) and (i%4 == 3) and (i%5 == 4) and (i%6 == 5):
       print(i)
       break

n = 0
for i in range(2000,2501,4):
    if  i%100 !=0 and i%4==0 or i%400 == 0 :
        print(i,end=" ")
        n+=1
    if n==4:
        print("")
        n=0



import random
import math

wins = 0
number = 10000

for p in range(0,number):
    a = []
    for i in range(0,100):
        a.append(i)
    random.shuffle(a)
#    print(a)

    NUM = 100
    WIN = 0
    LOOSE = 0
    flag = 0

    for i in range(0,NUM):
        k = i
        flag = 0
        for j in range(0,50):
            if a[k] == i:
                WIN+=1
                flag = 1
                break
            k = a[k]
        if flag == 0:
            LOOSE+=1

   # print("W:",WIN,' L:',LOOSE)
    if WIN == 100:
        wins+=1

print(wins/number)
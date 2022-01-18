import random

a = [[5,7],[9,11],[4,12],[5,0]]
interesnum = 4;
while interesnum > 0:
    delpos = random.randint(0, interesnum)
    print(delpos)
    a.pop(delpos)
    interesnum -= 1
    print(a)
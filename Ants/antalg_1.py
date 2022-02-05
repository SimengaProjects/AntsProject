import random

class Town:
    def __init__(self,pos = [200,200]):
        self.pos = pos
        self.fer = [0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]
        self.dist = []
towns = []
first = Town()
second = Town([200,300])
third = Town([300,300])
four = Town([400,400])
towns.append(first)
towns.append(second)
towns.append(third)
towns.append(four)
alpha = 1
beta = 1

for i in towns:
    for j in towns:
        if i!=j:
            i.dist.append(round(((j.pos[0]-i.pos[0])**2+(j.pos[1]-i.pos[1])**2)**0.5))

for i in towns:
    print(i.dist)



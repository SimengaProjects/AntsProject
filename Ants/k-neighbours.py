import random
import time
import pygame as pg
import math

RUN = 1
WIDTH = 1280
HEIGHT = 690
FPS = 30
ticks = 0
secunds = 0

pg.init()
pg.mixer.init()  # для звука
screen = pg.display.set_mode((WIDTH, HEIGHT),pg.DOUBLEBUF)
pg.display.set_caption("My Game")
clock = pg.time.Clock()

screen.set_alpha(None)

##ToDO:


def findmin(a):
    min = a[0]
    for i in a:
        if i<min:
            min = i
    return min
def scalarmult(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]
def findcos(v1,v2):
    mult = scalarmult(v1,v2)
    len1 = (v1[0]**2+v1[1]**2)**0.5
    len2 = (v2[0]**2+v2[1]**2)**0.5
    return(mult/(len1*len2))

def dist(first,second):
    return( round((((first[1]-second[1])**2+(first[0]-second[0])**2)**0.5)*100)/100 )

def findmaxindex(list):
    max = list[0]
    maxindex = 0
    index = -1
    for i in list:
        index+=1
        if i>max:
            max = i
            maxindex = index
    return maxindex



class Object:
    def __init__(self,pos = [100,100],type = 1,nav = 0,ymod = -1,k = 5):
        self.pos = pos
        self.type = type
        self.k = k
        self.nav = nav
        self.ymod = ymod
        self.speed = 0.2
    def movetonav(self):
        self.pos[0] += self.nav * self.speed
        if self.pos[0]>WIDTH-50 or self.pos[0]<50:
            self.nav*=-1
        self.pos[1] += (1 - (self.nav) ** 2) ** 0.5 * self.speed * self.ymod
        if self.pos[1]>HEIGHT-50 or self.pos[1]<50:
            self.ymod*=-1
    def drow(self):
        if self.type == 1:
            pg.draw.circle(screen,(220,150,0),self.pos,10,3)
        elif self.type == 2:
            pg.draw.circle(screen,(0,200,60),self.pos,10,3)
        else:
            pg.draw.circle(screen, (0, 0, 255), self.pos, 10,3)
#dont working
def check(obj,group):
    dists = []
    neighbours = []
    nums = [0,0,0]
    near = []

    for i in group:
        dists.append(dist(obj.pos,i.pos))
    dists.sort()
    for i in range(obj.k):
        neighbours.append(dists[i])
    for i in neighbours:
        for j in group:
            if i == dist(obj.pos,j.pos):
                near.append(j)
    for i in near:
        if i.type == 1:
            nums[0]+=1
        elif i.type == 2:
            nums[1]+=1
        else:
            nums[2]+=1
    #print(obj.type,'\t',nums,'\t',findmaxindex(nums))
    obj.type = findmaxindex(nums)+1


#Var's
if RUN:
    startTime = time.time()
    seconds = 0
    objects = []
    num = 300
    for i in range(num):
        pos = [random.randint(150,WIDTH-150),random.randint(150,HEIGHT-150)]
        type = random.randint(1,3)
        newObj = Object(pos,type,random.choice([-1,1])*random.random(),random.choice([-1,1]))
        objects.append(newObj)

#Game cicle
while RUN:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(1)
            if event.button == 2:
                print(2)
            if event.button == 3:
                print(3)
        if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    print("d")
                if event.key == pg.K_a:
                    print("a")
                if event.key == pg.K_s:
                    print("InteresNum = ",' ')
                    print("AntNum = ", ' ')
                    print("Food in home = ", ' ')
                if event.key == pg.K_w:
                    print("w")
                if event.key == pg.K_g:
                    print("g")

    screen.fill([0,0,0])
    for i in objects:
        i.drow()
        #i.movetonav()
    for i in range(5):
        check(random.choice(objects),objects)
    pg.draw.line(screen,(200,20,100),(40,40),(WIDTH-40,40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH-40, 40), (WIDTH - 40, HEIGHT-40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH-40, HEIGHT-40), (40, HEIGHT-40))
    pg.draw.line(screen, (200, 20, 100), (40, 40), ( 40, HEIGHT-40))
    pg.display.flip()
    t = time.time()
    if int(t-startTime) == seconds:
        seconds+=1


print("time: ",seconds-1)
pg.quit()
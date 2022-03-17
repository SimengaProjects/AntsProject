import random
import pygame as pg
import math
import time

RUN = 1
WIDTH = 1280
HEIGHT = 950
FPS = 60
ticks = 0
secunds = 0
GRAPH = [[0,0]]

pg.init()
pg.mixer.init()  # для звука
screen = pg.display.set_mode((WIDTH, HEIGHT),pg.DOUBLEBUF,1)
scr = pg.display.set_mode((WIDTH, HEIGHT),pg.DOUBLEBUF,1)
pg.display.set_caption("My Game")
clock = pg.time.Clock()

screen.set_alpha(None)

##ToDO:
#add +Home+ and food-eating sistems, add Quin and +aim's changing+.

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


class Creature:
    def __init__(self,pos = [WIDTH/2,HEIGHT/2],color = [255,255,255],type = 0,rad = 3,food = 100,speed = 1):
        self.pos = pos
        self.food = food
        self.speed = speed
        self.ymod = random.choice([-1,1])
        self.nav = random.randint(-1000,1000)/1000
        self.rad = rad
        self.color = color
        self.type = type
        self.birthnum = 1
    def move(self,change):
        self.pos[0]+=change[0]
        self.pos[1] += change[1]
    def randstep(self):
        self.pos[0] += random.choice([-1, 0, 1])
        self.pos[1] += random.choice([-1, 0, 1])
    def drow(self):
        pg.draw.circle(screen,self.color,self.pos,self.rad)
    def randnavchange(self):
        self.nav += random.randint(-3000,3000)/30000
        if self.nav>1:
            self.nav = 1
        if self.nav <-1:
            self.nav = -1
        if self.nav == 1 or self.nav == -1:
            self.ymod = -self.ymod
    def movetonav(self):
        self.pos[0] += self.nav * self.speed
        self.pos[1] += (1 - (self.nav) ** 2) ** 0.5 * self.speed * self.ymod

    def hungry(self,mod = 1):
        if self.type == 0:
            self.food += 1
        self.food-=self.type*2
def eat(arr,eater,food):
    if 0<eater.type-food.type<3:
        eater.food+=food.food/10
        arr.remove(food)

def dying(group):
    for k in group:
        if k.food<0:
            group.remove(k)

def tought(who1,who2):
    if abs(who1.pos[0]-who2.pos[0])<who1.rad+who2.rad:
        who2.pos[0]+= random.choice([-1,1]) * (who2.rad+who1.rad)
    if abs(who1.pos[1]-who2.pos[1])<who1.rad+who2.rad:
        who2.pos[1]+= random.choice([-1,1]) * (who2.rad+who1.rad)
def birth(parent,group,num = 1):
    if parent.food > 100 * (parent.type + 1):
        foodie = parent.food/(num+1)
        for j in range(0,num):
            new = Creature(parent.pos,parent.color,parent.type,parent.rad,foodie,parent.speed)
            if new.pos[0]<50: new.pos[0] = 50
            if new.pos[0]> WIDTH-50: new.pos[0] = WIDTH-50
            if new.pos[1]<50: new.pos[1] = 50
            if new.pos[1]> HEIGHT-50: new.pos[1] = HEIGHT-50
            group.append(new)
        parent.food = foodie

#Var's
if RUN:
    plants = []
    a = 0
    crnum = 3
    for i in range(crnum):
        ne = Creature([random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)],[30,200,30],0,3,100,0)
        plants.append(ne)



pg.event.set_allowed([pg.QUIT, pg.KEYDOWN, pg.MOUSEBUTTONDOWN])
scr.fill([0, 0, 0])
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

    for i in plants:
        if i.pos[0] < 50: i.pos[0] = 50
        if i.pos[0] > WIDTH - 50: i.pos[0] = WIDTH - 50
        if i.pos[1] < 50: i.pos[1] = 50
        if i.pos[1] > HEIGHT - 50: i.pos[1] = HEIGHT - 50
        i.drow()
        i.hungry()
        for j in plants:
            if i!=j:
                tought(i,j)
        #if random.randint(0,10) == 7:
    dying(plants)
    buffer = plants[:]
    for i in buffer:
        birth(i,plants,1)
    pg.draw.line(screen,(200,20,100),(40,40),(WIDTH-40,40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH-40, 40), (WIDTH - 40, HEIGHT-40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH-40, HEIGHT-40), (40, HEIGHT-40))
    pg.draw.line(screen, (200, 20, 100), (40, 40), ( 40, HEIGHT-40))
    pg.display.flip()
    ticks+=1
    if ticks == FPS/2:
        secunds+=0.5
        ticks = 0


print("time: ",secunds)

pg.quit()
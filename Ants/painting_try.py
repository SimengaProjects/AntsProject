import random
import pygame
import time
import numpy as np
import math

RUN = 1
WIDTH = 1200
HEIGHT = 900
FPS = 60
ticks = 0
secunds = 0

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

screen.set_alpha(None)
t = time.time()

class Obj:
    def __init__(self,pos = [WIDTH/2,HEIGHT/2],type = 0,speed = 0.5,nav = random.randint(0,1000)/1000):
        self.pos = pos
        self.type = type
        self.color = [type*100,50,200-type*100]
        self.nav = nav
        self.y = random.choice([-1,1])
        self.speed = speed
        self.greenup = 2
    def drow(self):
        pygame.draw.circle(screen,self.color,self.pos,1)
    def colorchange(self):
        if self.color[1] >= 200:
            self.greenup = -2
        if self.color[1] <= 10:
            self.greenup = 2
        self.color[1]+=self.greenup
    def randspeedchange(self):
        self.speed+=random.randint(-1000,1000)/500000
    def randnavchange(self):
        self.nav+=random.randint(-10000,10000)/50000
        if self.nav>1:
            self.nav = 1
            self.y*=-1
        if self.nav<-1:
            self.nav = -1
            self.y*=-1
    def move(self):
        self.pos[0]+=self.speed*self.nav
        self.pos[1]+=self.y*self.speed*(1-self.nav**2)**0.5
    def movecord(self,x,y):
        self.pos[0]+=x
        self.pos[1]+=y

def dist(first,second):
    return( round((((first[1]-second[1])**2+(first[0]-second[0])**2)**0.5)))

def CreateObj(mass,pos,type,sp,nav):
    o = Obj(pos,type,sp,nav)
    mass.append(o)


#Global activity:
ABSX = 0.02
ABSY = -0.05

go = 1
painting = 1
onum = 30
tickes = 0
zerotime = 51
maxnear = 10
nearrange = 50
objects = []
for i in range (0,onum):
    o = Obj([random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)],random.choice([0,1,2]))
    #o.color = [random.randint(0,255),random.randint(0,180),random.randint(0,255)]
    objects.append(o)

#Game cicle
while RUN:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(onum)
            if event.button == 2:
                print(2)
                pygame.display.flip()
            if event.button == 3:
                print(3)
            if event.button == 4:
                print(4)
            if event.button == 5:
                print(5)
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    print(len(objects))
                if event.key == pygame.K_a:
                    print("a")
                    painting*=-1
                if event.key == pygame.K_s:
                    print("InteresNum = ",' ')
                    print("AntNum = ", ' ')
                    print("Food in home = ", ' ')
                if event.key == pygame.K_w:
                    print("w")
                if event.key == pygame.K_g:
                    print(go)
                    go *=-1

    if painting>0:
        screen.fill([0,0,0])
    #zerotime += 10
    if go>0:
        for i in objects:
            nears = 0
            for j in objects:
                if i.type == j.type and dist(i.pos,j.pos)<nearrange and i!=j:
                    nears+=1
                if nears>maxnear:
                    objects.remove(j)
                    #print("del")
                    onum+=-1
            if random.randint(0,1000) == 666:
                CreateObj(objects,i.pos[:],i.type,i.speed,i.nav)
                onum+=1
                #print(i.type)
            i.move()
            i.movecord(ABSX,ABSY)
            #i.colorchange()
            if i.pos[0]>WIDTH-50:
                i.nav*=-1
                i.pos[0] = WIDTH-50
            if  i.pos[0]<50:
                i.nav *= -1
                i.pos[0] =50
            if i.pos[1] > HEIGHT - 50:
                i.nav *= -1
                i.pos[1] = HEIGHT - 50
            if i.pos[1] < 50:
                i.nav *= -1
                i.pos[1] = 50
            i.randnavchange()
            i.randspeedchange()
            i.drow()
        pygame.draw.line(screen,(200,20,100),(40,40),(WIDTH-40,40))
        pygame.draw.line(screen, (200, 20, 100), (WIDTH-40, 40), (WIDTH - 40, HEIGHT-40))
        pygame.draw.line(screen, (200, 20, 100), (WIDTH-40, HEIGHT-40), (40, HEIGHT-40))
        pygame.draw.line(screen, (200, 20, 100), (40, 40), ( 40, HEIGHT-40))
        pygame.display.flip()
    tickes+=1
    ticks+=1
    if ticks == FPS/5:
        secunds+=0.2
        ticks = 0
print("time: ",secunds)
te = time.time()
print("real time:",te-t)
pygame.quit()
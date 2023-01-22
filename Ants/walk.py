import random
import time
import pygame
import math
import numpy as np

RUN = 1
WIDTH = 1280
HEIGHT = 690
FPS = 20
ticks = 0
secunds = 0

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.DOUBLEBUF)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

screen.set_alpha(None)

##ToDO:


def findmin(a):
    min = a[0]
    for i in a:
        if i<min:
            min = i
    return min
def scalarmult(v1,v2):
    #ve1 = np.array(v1)
    #ve2 = np.array(v2)
    return v1.dot(v2)
def easyfindcos(v1,v2):
    mult = v1[0]*v2[0]+v1[1]*v2[1]
    len1 = (v1[0] + v1[1])
    len2 = (v2[0] + v2[1])
    return (mult / (len1 * len2)) / 1, 2

# def findcos(v1, v2):
#     return easyfindcos(v1, v2)

def findcos(v1,v2):
    mult = scalarmult(v1,v2)
    #len1 = (v1[0]**2+v1[1]**2)**0.5
    #len2 = (v2[0]**2+v2[1]**2)**0.5
    len1 = 1
    len2 = 1
    return(mult/(len1*len2))

def easydist(first,second):
    return (abs(abs(first[1])-abs(second[1])) + abs(abs(first[0])-abs(second[0]))) / 1.2
def dist(first,second):
    return easydist(first,second)
    #return( round((((first[1]-second[1])**2+(first[0]-second[0])**2)**0.5)*100)/100 )


class Ants:
    def __init__(self, pos,nav =0.7,ymod = 1,speed = 1):
        self.steps = [0,0]
        self.color = [200,200,200]
        self.pos = pos
        self.speed = speed
        self.rad = 3
        self.nav = nav
        self.ymod = ymod
        self.aim = 1
    def drow(self):
        pygame.draw.circle(screen, self.color, self.pos, self.rad)
    def move(self,x,y):
        self.pos[0]= self.pos[0]+x
        self.pos[1]=self.pos[1]+y
    def randnavchange(self):
        self.nav += random.randint(-1000,1000)/1500
        if self.nav>1:
            self.nav = 1
        if self.nav <-1:
            self.nav = -1
        if self.nav == 1 or self.nav == -1:
            self.ymod = -self.ymod
    def navchange(self,x,y):
        self.nav[0] = x
        self.ymod = y
    def takenav(self,objpos):
        if objpos[1]>self.pos[1]:
            self.ymod = 1
        else:
            self.ymod = -1
        #try:
        #distantion = dist(self.pos,objpos)
        if dist!= 0:
            #vector1 = [(-self.pos[0]+objpos[0])/distantion,(-self.pos[1]+objpos[1])/distantion]
            vector1 = np.array([objpos[0]-self.pos[0],objpos[1]-self.pos[1]])
            #print(vector1)
            vector1 = vector1 / np.linalg.norm(vector1)
            #print(vector1)
            vector2 = np.array([1,0])
            self.nav = findcos(vector1,vector2)
        #except:
            #print("TakeNav error!")
    def movetonav(self):
        self.pos[0]+=self.nav*self.speed
        self.pos[1]+=(1-(self.nav)**2)**0.5 * self.speed * self.ymod
        if self.pos[0]<50 or self.pos[0]>WIDTH-50:
            self.nav*=-1
        if self.pos[1] < 50 or self.pos[1] > HEIGHT - 50:
            self.ymod*=-1
    def steptoobj(self,objpos):
        if abs(self.pos[0]-objpos[0])>abs(self.pos[1]-objpos[1]):
            if objpos[0]<self.pos[0]:
                gox = -self.speed *(1-((self.pos[1] - objpos[1])/(self.pos[0] - objpos[0]))**2)**0.5
            elif objpos[0] > self.pos[0] :
                gox = self.speed * (1-((self.pos[1] - objpos[1])/(self.pos[0] - objpos[0]))**2)**0.5
            else:
                gox = 0;
            if objpos[1]<self.pos[1]:
                goy = -self.speed* abs(self.pos[1] - objpos[1])/abs(self.pos[0] - objpos[0])
            elif objpos[1] > self.pos[1] :
                goy = self.speed* abs(self.pos[1] - objpos[1])/abs(self.pos[0] - objpos[0])
            else:
                goy = 0;
            self.move(gox,goy)
        elif abs(self.pos[0] - objpos[0]) < abs(self.pos[1] - objpos[1]):
            if objpos[0] < self.pos[0]:
                gox = -self.speed * abs(self.pos[0] - objpos[0])/ abs(self.pos[1] - objpos[1])
            elif objpos[0] > self.pos[0]:
                gox = self.speed * abs(self.pos[0] - objpos[0])/ abs(self.pos[1] - objpos[1])
            else:
                gox = 0
            if objpos[1] < self.pos[1]:
                goy = -self.speed * (1 -(abs(self.pos[0] - objpos[0])/ abs(self.pos[1] - objpos[1]))**2)**0.5
            elif objpos[1] > self.pos[1]:
                goy = self.speed * (1 -(abs(self.pos[0] - objpos[0])/ abs(self.pos[1] - objpos[1]))**2)**0.5
            else:
                goy = 0
            self.move(gox, goy)
    def randstep(self):
        gox = random.choice((-1,1))
        goy = random.choice((-1, 1))
        self.move(gox, goy)

#Var's
if RUN:
    startTime = time.time()
    seconds = 0
    antNum = 500
    ants = []
    startPos = [200,HEIGHT//2]
    for i in range(antNum):
        newAnt = Ants(startPos,1)
        newAnt.speed = 0.03
        ants.append(newAnt)

#Game cicle
while RUN:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(1)
            if event.button == 2:
                print(2)
            if event.button == 3:
                print(3)
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    print("d")
                if event.key == pygame.K_a:
                    print("a")
                if event.key == pygame.K_s:
                    print("InteresNum = ",' ')
                    print("AntNum = ", ' ')
                    print("Food in home = ", ' ')
                if event.key == pygame.K_w:
                    print("w")
                if event.key == pygame.K_g:
                    print("g")

    screen.fill([0,0,0])

    for ant in ants:
        ant.drow()
        ant.movetonav()
        ant.randnavchange()

    pygame.draw.line(screen,(200,20,100),(40,40),(WIDTH-40,40))
    pygame.draw.line(screen, (200, 20, 100), (WIDTH-40, 40), (WIDTH - 40, HEIGHT-40))
    pygame.draw.line(screen, (200, 20, 100), (WIDTH-40, HEIGHT-40), (40, HEIGHT-40))
    pygame.draw.line(screen, (200, 20, 100), (40, 40), ( 40, HEIGHT-40))
    pygame.display.flip()
    t = time.time()
    if int(t-startTime) == seconds:
        seconds+=1


print("time: ",seconds-1)
pygame.quit()
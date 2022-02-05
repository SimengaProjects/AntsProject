import random
import pygame
import math

RUN = 1
WIDTH = 1024
HEIGHT = 800
FPS = 50

generatorON = 1
antnum = 10
size = (3,3)
interesnum = 10
homefood = 0
gennum = 5

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

class Interespoint:
    def __init__(self,pos,speed = [0.3,0],chit=0):
        self.pos = pos
        self.speed = speed
        if chit == 0:
            self.food = random.randint(5,60)*10
        else:
            self.food = random.randint(50, 60) * 1000
    def Move(self):
        if self.pos[0]>50 and self.pos[0]<WIDTH-50:
            self.pos[0]+=self.speed[0]
        else:
            self.speed[0]=-self.speed[0]
            self.pos[0]+=3*self.speed[0]
        if self.pos[1]>50 and self.pos[1]<HEIGHT-50:
            self.pos[1]+=self.speed[1]
        else:
            self.speed[1]=-self.speed[1]
            self.pos[1]+=3*self.speed[1]


def findmin(a):
    min = a[0]
    for i in a:
        if i<min:
            min = i
    return min

def dist(first,second):
    return( round((((first[1]-second[1])**2+(first[0]-second[0])**2)**0.5)*100)/100 )

class Ants:
    def __init__(self, pos,speed = 1):
        self.pos = pos
        self.food = 0
        self.life = random.randint(150,400)
        self.gohome = 0;
        self.speed = speed
    def move(self,x,y):
        self.pos[0]+=x
        self.pos[1]+=y
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
maxsp = 0
s = 1
c = 3
a = Ants([50,50],3)
b = Interespoint([500,500],[0,0],0)
ymod = HEIGHT/WIDTH
lastd = a.pos
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
                print("___")
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
                    if generatorON == 0:
                        generatorON = 1
                    else:
                        generatorON = 0

    screen.fill([0,0,0])
    d = dist(a.pos,b.pos)
    a.steptoobj(b.pos)
    b.pos[0]-=s
    b.pos[1] += c
    if dist(a.pos,lastd)>maxsp:
        maxsp = dist(a.pos,lastd)
    lastd =a.pos[:]
    if b.pos[0] > 600 or b.pos[0]<50:
        s = -s
    if b.pos[1] > 600 or b.pos[1]<50:
        c = -c
    pygame.draw.circle(screen,(255,0,0),a.pos,10)
    pygame.draw.circle(screen, (255, 0, 255), b.pos, 10)
    pygame.display.flip()
print(maxsp)
pygame.quit()
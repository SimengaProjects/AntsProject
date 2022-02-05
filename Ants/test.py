import random
import pygame
import math

RUN = 1
WIDTH = 1024
HEIGHT = 800
FPS = 30
ticks = 0
secunds = 0

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
    def __init__(self, pos,nav =0.7,ymod = 1,speed = 1):
        self.steps = [0,0]
        self.color = [200,200,200]
        self.pos = pos
        self.speed = speed
        self.rad = 2
        self.nav = nav
        self.ymod = ymod
    def drow(self):
        pygame.draw.circle(screen, self.color, self.pos, self.rad)
    def move(self,x,y):
        self.pos[0]= self.pos[0]+x
        self.pos[1]=self.pos[1]+y
    def randnavchange(self):
        self.nav += random.randint(-666, 666) / 100000
        if self.nav == 1 or self.nav == -1:
            self.ymod = -self.ymod
    def navchange(self,x):
        self.nav[0] = x
    def movetonav(self):
        self.pos[0]+=self.nav*self.speed
        self.pos[1]+=(1-(self.nav)**2)**0.5 * self.speed * self.ymod
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

def CreateAnt(colony,pos,speed = 1):
    a = Ants(pos,speed)
    colony.append(a)
def Scream(colony,screamer,state):
    for i in colony:
        if dist(i.pos,screamer.pos)<screamrange:
            if screamer.steps[state] < i.steps[state]:
                i.steps[state] = screamer.steps[state]
                # make moving changer to screamer


#Var's
if RUN:
    home = [WIDTH/4,HEIGHT/3]
    screamrange = 50
    antnum = 55
    ants = []
    for i in range(0,antnum):
        cord = home[:]
        CreateAnt(ants,cord)



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
                    print("g")

    screen.fill([0,0,0])

    for i in ants:
        i.randstep()
        i.drow()
    pygame.display.flip()
    ticks+=1
    if ticks == FPS:
        secunds+=1
        ticks = 0

print("time: ",secunds)
pygame.quit()
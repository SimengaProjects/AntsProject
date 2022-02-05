import random
import pygame
import math

RUN = 1
WIDTH = 1024
HEIGHT = 720
FPS = 30
ticks = 0
secunds = 0

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

##ToDO:
#add Home and doof-eating sistems, add Quin and aim's changing.

class Interespoint:
    def __init__(self,pos,speed = [0,0],chit=0):
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
def scalarmult(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]
def findcos(v1,v2):
    mult = scalarmult(v1,v2)
    len1 = (v1[0]**2+v1[1]**2)**0.5
    len2 = (v2[0]**2+v2[1]**2)**0.5
    return(mult/(len1*len2))

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
        self.nav += random.randint(-3000,3000)/100000
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
        distantion = dist(self.pos,objpos)
        vector1 = [(-self.pos[0]+objpos[0])/distantion,(-self.pos[1]+objpos[1])/distantion]
        vector2 = [1,0]
        self.nav = findcos(vector1,vector2)
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

def CreateAnt(colony,pos,nav = 0.7,ymod = 1,speed = 1):
    a = Ants(pos,nav,ymod,speed)
    colony.append(a)
def Scream(colony,screamer,state):
    for i in colony:
        if screamer != i and 1 and dist(i.pos,screamer.pos)<screamrange and screamer.steps[state]+screamrange < i.steps[state]:
                    i.steps[state] = screamer.steps[state]+screamrange
                    i.takenav(screamer.pos)
                    pygame.draw.line(screen,(80,5,180),screamer.pos,i.pos)


#Var's
if RUN:
    screams = []
    l = []
    ints = []
    home = [WIDTH/2,HEIGHT/2]
    screamrange = 40
    interesnum = 3
    antnum = 250
    ants = []
    for i in range(0,antnum):
        cord = home[:]
        CreateAnt(ants,[random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)],round(random.randint(-50,50)/50*1000)/1000*random.choice([-1,1]),random.choice([1,-1]),5)
    for i in range(0,interesnum):
        interes = Interespoint([random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)])
        ints.append(interes)


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
    for i in ints:
        pygame.draw.circle(screen, (0, 200, 200), i.pos, 10)
    for i in ants:
        Scream(ants,i,1)
        i.movetonav()
        i.steps[0]+=1
        i.steps[1]+=1
        i.randnavchange()

        if i.pos[0]< 50 or i.pos[0]>WIDTH-50:
            i.nav = -i.nav
        if i.pos[1]<50 or i.pos[1]>HEIGHT-50:
            i.ymod = -i.ymod
        for j in ints:
            if dist(i.pos,j.pos)<10:
                i.steps[1] = 0
                i.color = (255,0,0)
        i.drow()
    pygame.display.flip()
    ticks+=1
    if ticks == FPS:
        secunds+=1
        ticks = 0

print("time: ",secunds)
pygame.quit()
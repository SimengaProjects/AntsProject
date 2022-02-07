import random
import pygame
import math

RUN = 1
WIDTH = 1280
HEIGHT = 690
FPS = 60
ticks = 0
secunds = 0

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.DOUBLEBUF)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

screen.set_alpha(None)

##ToDO:
#add +Home+ and food-eating sistems, add Quin and +aim's changing+.

class Interespoint:
    def __init__(self,pos,aimpoint = 1,speed = [0,0],chit=0):
        self.pos = pos
        self.aimpoint = aimpoint
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
        self.rad = 1
        self.nav = nav
        self.ymod = ymod
        self.aim = 1
    def drow(self):
        pygame.draw.circle(screen, self.color, self.pos, self.rad)
    def move(self,x,y):
        self.pos[0]= self.pos[0]+x
        self.pos[1]=self.pos[1]+y
    def randnavchange(self):
        self.nav += random.randint(-3000,3000)/500000
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


#Var's
if RUN:
    showline = 1
    fmb = 0
    screams = []
    screamsuperrange = 80
    screamersnum = 30
    for i in range(0,screamersnum):
        CreateAnt(screams, [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)],
                  round(random.randint(-50, 50) / 50 * 1000) / 1000 * random.choice([-1, 1]), random.choice([1, -1]),
                  random.randint(20, 100) / 100)
        screams[i].rad = 3
        screams[i].speed*=2
        screams[i].color = (50,100,255)
    l = []
    ints = []
    home = Interespoint([WIDTH/2,HEIGHT/2],0)
    home.pos = [random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)]
    interesnum = 2
    antnum = 350
    #screamrange = 1/(80*antnum/(WIDTH*HEIGHT))
    screamrange = 40
    print(screamrange)
    ants = []
    for i in range(0,antnum):
        CreateAnt(ants,[random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)],round(random.randint(-50,50)/50*1000)/1000*random.choice([-1,1]),random.choice([1,-1]),random.randint(40,1000)/1000)
    for i in range(0,interesnum):
        interes = Interespoint([random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)])
        #interes.pos = [WIDTH/5*3,HEIGHT/2]
        ints.append(interes)


def Scream(colony,screamer,state,screamrange = screamrange):
    for i in colony:
        if screamer != i and dist(i.pos,screamer.pos)<screamrange and screamer.steps[state]+screamrange < i.steps[state]:
                    i.steps[state] = screamer.steps[state]+screamrange
                    Scream(ants, i, state)
                    if state == 0:
                        Scream(screams,i,0)
                    if i.aim == state:
                        i.takenav(screamer.pos)
                        if showline == 1:
                            pygame.draw.line(screen,(100*state,10,250-100*state),screamer.pos,i.pos)

#Game cicle
while RUN:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(1)
                counter = 0
                for i in ants:
                    if dist(i.pos,list(event.pos))<100:
                        counter+=1
                print(counter)
                fmb = list(event.pos)
                fmbrad = 100
            if event.button == 2:
                print(2)
                counter = 0
                for i in ants:
                    if dist(i.pos,list(event.pos))<screamrange:
                        counter+=1
                print(counter)
                fmb = list(event.pos)
                fmbrad = screamrange
            if event.button == 3:
                print(3)
                counter = 0
                for i in ants:
                    if dist(i.pos,list(event.pos))<10:
                        counter+=1
                print(counter)
                fmb = list(event.pos)
                fmbrad = 10
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    print("d")
                    showline*=-1
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
    if fmb != 0:
        pygame.draw.circle(screen, (255, 255, 0), fmb, fmbrad)
        fmb = 0
        fmbrad = 0
    for i in ints:
        pygame.draw.circle(screen, (0, 200, 200), i.pos, 10)
    pygame.draw.circle(screen,(50,255,50),home.pos,15)
    for i in screams:
        Scream(ants,i,random.choice([0,1]),screamsuperrange)
        i.movetonav()
        for j in ints:
            if dist(i.pos,j.pos)<10:
                i.steps[1] = 0
                i.nav=-i.nav
                i.ymod*=-1
        if dist(i.pos,home.pos)<15:
            i.steps[0] = 0
            i.aim = 1
            i.nav = -i.nav
            i.ymod *= -1
        if i.pos[0]< 50 or i.pos[0]>WIDTH-50:
            i.nav = -i.nav
        if i.pos[1]<50 or i.pos[1]>HEIGHT-50:
            i.ymod = -i.ymod
        i.steps[0]+=1
        i.steps[1]+=1
        for k in range(0,10):
            i.randnavchange()
        i.drow()
    for i in ants:
        #Scream(ants, i, random.choice([0,1]))
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
                if random.randint(0, 5) == 3:
                    Scream(ants, i, 1)
                if  i.aim == 1:
                    i.aim = 0
                    i.color = (255,0,0)
                    i.nav=-i.nav
                    i.ymod*=-1
        if dist(i.pos,home.pos)<15:
            i.steps[0] = 0
            if random.randint(0,10) == 6:
                Scream(ants, i, 0)
            if  i.aim == 0:
                i.aim = 1
                i.color = (0,0,255)
                i.nav = -i.nav
                i.ymod *= -1
        i.drow()
    pygame.draw.line(screen,(200,20,100),(40,40),(WIDTH-40,40))
    pygame.draw.line(screen, (200, 20, 100), (WIDTH-40, 40), (WIDTH - 40, HEIGHT-40))
    pygame.draw.line(screen, (200, 20, 100), (WIDTH-40, HEIGHT-40), (40, HEIGHT-40))
    pygame.draw.line(screen, (200, 20, 100), (40, 40), ( 40, HEIGHT-40))
    pygame.display.flip()
    ticks+=1
    if ticks == FPS:
        secunds+=1
        ticks = 0

print("time: ",secunds)
pygame.quit()
import random
import pygame
import math

RUN = 1
WIDTH = 640
HEIGHT = 640
FPS = 30

generatorON = 1
antnum = 100
size = (3,3)
interesnum = 10
homefood = 0

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

class Interespoint:
    def __init__(self,pos):
        self.pos = pos
        self.food = random.randint(5,60)*10

def findmin(a):
    min = a[0]
    for i in a:
        if i<min:
            min = i
    return min

def dist(first,second):
    return( round((((first[1]-second[1])**2+(first[0]-second[0])**2)**0.5)*100)/100 )

class Ants:
    def __init__(self, pos):
        self.pos = pos
        self.food = 0
        self.life = random.randint(150,400)
        self.gohome = 0;
    def move(self,x,y):
        self.pos[0]+=x
        self.pos[1]+=y
    def steptoobj(self,objpos):
        if objpos[0]<self.pos[0]:
            gox = -1
        elif objpos[0] > self.pos[0] :
            gox = 1
        else:
            gox = 0;
        if objpos[1]<self.pos[1]:
            goy = -1
        elif objpos[1] > self.pos[1] :
            goy = 1
        else:
            goy = 0;
        self.move(gox,goy)
    def randstep(self):
        gox = random.choice((-1,1))
        goy = random.choice((-1, 1))
        self.move(gox, goy)

ant = []
color=[]
nearestinterespoint = []

home = [200,200]

#create ants

for i in range(0,antnum):
    pos = [random.randint(20,620) , random.randint(50,620)]
    ants = Ants(pos)
    ant.append(ants)
    #color.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    color.append((255,255,255))
#create food
interespoint = []
for i in range(0,interesnum):
    interes = Interespoint([random.randint(50,550),random.randint(50,550)])
    interespoint.append(interes)


#Game cicle
while RUN:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                interes = Interespoint(event.pos)
                interespoint.append(interes)
                interesnum += 1
            if event.button == 3:
                if interesnum>1:
                    path2 = []
                    for j in range(0, interesnum):
                        path2.append(dist(event.pos, interespoint[j].pos))
                    print(path2)
                    print( path2.index(findmin(path2)))
                    near2 = path2.index(findmin(path2))
                    interespoint.pop(near2)
                    interesnum-=1
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for i in range(0,interesnum):
                        interespoint[i].pos= [random.randint(50,550),random.randint(50,550)]
                if event.key == pygame.K_d:
                    if interesnum>0:
                        delpos = random.randint(0,interesnum-1)
                        interespoint.pop(delpos)
                        interesnum-=1
                if event.key == pygame.K_a:
                    interes = Interespoint([random.randint(50, 550), random.randint(50, 550)])
                    interespoint.append(interes)
                    interesnum+=1
                if event.key == pygame.K_s:
                    print("InteresNum = ",interesnum,' ')
                    print("AntNum = ", antnum, ' ')
                    print("Food in home = ", homefood, ' ')
                if event.key == pygame.K_w:
                    ant.clear()
                    color.clear()
                    for i in range(0, antnum):
                        pos = [random.randint(20, 620), random.randint(50, 620)]
                        ants = Ants(pos)
                        ant.append(ants)
                        #color.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
                        color.append((255, 255, 255))
                if event.key == pygame.K_g:
                    if generatorON == 0:
                        generatorON = 1
                    else:
                        generatorON = 0

    screen.fill([0,0,0])
    i = 0
    if (generatorON == 1) and (interesnum<1):
        interes = Interespoint([random.randint(50, 550), random.randint(50, 550)])
        interespoint.append(interes)
        interes = Interespoint([random.randint(50, 550), random.randint(50, 550)])
        interespoint.append(interes)
        interesnum += 2
    while (i<antnum) and (ant!=[]):
        if ant[i].food > 100:
            ant[i].gohome = 1
            color[i] = (255,20,240)
        if ant[i].life <0:
            antnum-=1
            ant.pop(i)
            color.pop(i)
        else:
            ant[i].life-=1

        i+=1
    i = 0
    try:
        while i<interesnum:
            if (random.randint(0, 10000) == 666) and (interesnum > 1):
                interespoint.pop(i)
                interesnum -= 1
            if (interespoint[i].food<0):
                interespoint.pop(i)
                interesnum -= 1
            i+=1
    except:
        print()
    for i in range(0, interesnum):
        pygame.draw.circle(screen, (100, 0, 0), interespoint[i].pos, 20)
    for i in range(0,antnum):
        if (ant[i].pos[0] > 610):
            ant[i].pos[0] = 610
        if (ant[i].pos[0] < 10):
            ant[i].pos[0] = 10
        if (ant[i].pos[1] > 610):
            ant[i].pos[1] = 610
        if (ant[i].pos[1] < 10):
            ant[i].pos[1] = 10

        r = pygame.Rect(ant[i].pos[0], ant[i].pos[1],size[0],size[1])
        try:
            path = []
            for j in range(0,interesnum):
                path.append(dist(ant[i].pos,interespoint[j].pos))
            near = interespoint[path.index(findmin(path))].pos
            if findmin(path) < 20:
                ant[i].food+=1
                interespoint[path.index(findmin(path))].food-=1
            if ant[i].life<100 and ant[i].food>0:
                ant[i].food-=1
                ant[i].life+=5
            nearestinterespoint = [near[0],near[1]]
            if ant[i].gohome == 0:
                ant[i].steptoobj(nearestinterespoint)
            else:
                ant[i].steptoobj(home)
        except:
            ant[i].steptoobj(home)
        if (ant[i].gohome == 1) and (dist(ant[i].pos, home) < 30):
            color[i] = (255, 255, 255)

            if homefood > 100:
                homefood += ant[i].food - findmin(path)/12
                ant[i].life += findmin(path)*10
                ant[i].food = 0
            else:
                homefood += ant[i].food
                ant[i].food = 0
            ant[i].gohome = 0
        for j in range (0,antnum):
            if i!=j:
                if ((abs(ant[i].pos[0]-ant[j].pos[0])<size[0]) and (abs(ant[i].pos[1]-ant[j].pos[1])<size[1])):
                    ant[j].move(random.choice((-10,10)),random.choice((-10,10)))
            pygame.draw.rect(screen, color[i], r)

    if homefood>150:
        homefood-=150
        newant = Ants([200,200])
        antnum+=1
        ant.append(newant)
        color.append((100, 200, 200))

    pygame.draw.circle(screen,(0,200,200),home,30)
    pygame.display.flip()

pygame.quit()
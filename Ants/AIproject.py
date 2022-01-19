import pygame
import random

RUN = 1
WIDTH = 1024
HEIGHT = 800
FPS = 60

#initialization of pygame
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

        #classes
#Zones
class DangerZone:
    def __init__(self,pos= [-100,-100],rad = 50,lp=random.random(),rp=random.random(),up=random.random(),dp=random.random()):
        self.pos = pos
        self.rad = rad
        self.lp = lp
        self.rp = rp
        self.up = up
        self.dp = dp

class Interespoint:
    def __init__(self,pos = [random.randint(30,WIDTH-30),random.randint(30,HEIGHT-30)],rad = 3):
        self.pos = pos
        self.rad = rad
#Persons
class Ant:
    def __init__(self,pos = [random.randint(30,WIDTH-30),random.randint(30,HEIGHT-30)],speed = 3,life=500):
        self.pos = pos
        self.life = life
        self.speed = speed
        self.food = 0
    def leftstep(self):
        self.pos[0]-=self.speed
    def rightstep(self):
        self.pos[0]+=self.speed
    def upstep(self):
        self.pos[0]-=self.speed
    def downstep(self):
        self.pos[0]+=self.speed
    def move(self, x, y):
        self.pos[0] += x
        self.pos[1] += y
    def steptoobj(self, objpos):
        if objpos[0] < self.pos[0]:
            gox = -self.speed
        elif objpos[0] > self.pos[0]:
            gox = self.speed
        else:
            gox = 0;
        if objpos[1] < self.pos[1]:
            goy = -self.speed
        elif objpos[1] > self.pos[1]:
            goy = self.speed
        else:
            goy = 0;
        self.move(gox, goy)
        #defs

def findmin(a):
    min = a[0]
    for i in a:
        if i<min:
            min = i
    return min

def dist(first,second):
    return( round((((first[1]-second[1])**2+(first[0]-second[0])**2)**0.5)*100)/100 )

#var's
if RUN:
    interestes = []
    dans = []
    ants = []
    foodtimer = 0
    dannum = 1
    for i in range(0,dannum):
        dan = DangerZone([600,400])
        dans.append(dan)
    intnum = 70
    internum = intnum
    for i in range(0,intnum):
        interes = Interespoint([random.randint(30,WIDTH-30),random.randint(30,HEIGHT-30)])
        interestes.append(interes)
    antnum = 3
    for i in range(0,antnum):
        ant = Ant([random.randint(30,WIDTH-30),random.randint(30,HEIGHT-30)])
        ants.append((ant))

while RUN:
    clock.tick(FPS)
#Keys
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
                if event.key == pygame.K_SPACE:
                    print("Sp")
                if event.key == pygame.K_d:
                    print("d")
                if event.key == pygame.K_a:
                    print("a")
                if event.key == pygame.K_s:
                    print("statistic:")
                    print("ant's num=",antnum)
                    max = 0
                    mid = 0
                    for num in range(0,antnum):
                        mid+=ants[num].speed
                        if ants[num].speed>max:
                            max =ants[num].speed
                    mid = round(mid/antnum,3)
                    print("Max speed is ",max,"averrange speed is ",mid)


                if event.key == pygame.K_w:
                    print("w")
                if event.key == pygame.K_g:
                    print("g")

    screen.fill([0,0,0])
    for i in range(0,antnum):
        path = []
        for j in range(0, intnum):
            path.append(dist(ants[i].pos, interestes[j].pos))
        near = interestes[path.index(findmin(path))].pos
        nearestinterespoint = [near[0], near[1]]
        ants[i].steptoobj(nearestinterespoint)
        if dist(ants[i].pos,interestes[path.index(findmin(path))].pos)<5+ants[i].speed/2:
            interestes.pop(path.index(findmin(path)))
            intnum-=1
            ants[i].food +=1
            ants[i].life+=5
        for kicking in range(0,antnum):
            if dist(ants[i].pos,ants[kicking].pos)<20 and i!=kicking:
                kick = [random.choice([-6,6]),random.choice([-6,6])]
                ants[kicking].move(kick[0],kick[1])
        if ants[i].food == 20:
            ants[i].life+=100
            if ants[i].speed<10 and ants[i].speed>0:
                chan = random.randint(0,10)
                if chan == 7:
                    bonus = 1
                elif chan == 6:
                    bonus = -1
                else:
                    bonus = 0
            ant = Ant(ants[i].pos[:],ants[i].speed+bonus)
            ants.append((ant))
            antnum+=1
            ants[i].food-=20
    i = 0
    while (i < antnum) and (ants != []):
        if ants[i].life < 0:
            maxkk = int(ants[i].food/2)
            for kk in range(0,maxkk):
                interes = Interespoint(ants[i].pos[:])
                interestes.append(interes)
                intnum += 1
            antnum -= 1
            ants.pop(i)
        else:
            ants[i].life -= 1
        i+=1

    if intnum == 1:
        interes = Interespoint([random.randint(30, WIDTH - 30), random.randint(30, HEIGHT - 30)])
        interestes.append(interes)
        intnum+=1
    if foodtimer>FPS:
        for addfood in range(0,internum-intnum):
            interes = Interespoint([random.randint(30, WIDTH - 30), random.randint(30, HEIGHT - 30)])
            interestes.append(interes)
            intnum += 1
    else:
        foodtimer+=1

    for i in range(0, antnum):
        pygame.draw.circle(screen,(200,80,50),ants[i].pos,5)
    for i in range(0, intnum):
        pygame.draw.circle(screen,(20,200,50),interestes[i].pos,interestes[i].rad)


    pygame.display.flip()

pygame.quit()
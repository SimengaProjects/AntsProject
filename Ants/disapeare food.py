import random
import pygame
import math

RUN = 1
WIDTH = 640
HEIGHT = 640
FPS = 30

antnum = 500
size = (3,3)
interesnum = 6

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()



def findmin(a):
    min = a[0];
    for i in a:
        if i<min:
            min = i
    return min

def dist(first,second):
    return( round((((first[1]-second[1])**2+(first[0]-second[0])**2)**0.5)*100)/100 )

class Ants:
    def __init__(self, pos):
        self.pos = pos
        self.pheromone = 0;
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

interespointpos = []

#create ants

for i in range(0,antnum):
    pos = [random.randint(20,620) , random.randint(50,620)]
    ants = Ants(pos)
    ant.append(ants)
    #color.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    color.append((255,255,255))
#create food
for i in range(0,interesnum):
    interespointpos.append([random.randint(50,550),random.randint(50,550)])


#Game cicle
while RUN:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                interespointpos.append(event.pos)
                interesnum += 1
            if event.button == 3:
                if interesnum>1:
                    path2 = []
                    for j in range(0, interesnum):
                        path2.append(dist(event.pos, interespointpos[j]))
                    print(path2)
                    print( path2.index(findmin(path2)))
                    near2 = path2.index(findmin(path2))
                    interespointpos.pop(near2)
                    interesnum-=1
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for i in range(0,interesnum):
                        interespointpos[i] = [random.randint(50,550),random.randint(50,550)]
                if event.key == pygame.K_d:
                    if interesnum>1:
                        delpos = random.randint(0,interesnum-1)
                        interespointpos.pop(delpos)
                        interesnum-=1
                if event.key == pygame.K_a:
                    interespointpos.append([random.randint(50, 550), random.randint(50, 550)])
                    interesnum+=1
                if event.key == pygame.K_s:
                    print("InteresNum = ",interesnum,' ')
                if event.key == pygame.K_w:
                    ant.clear()
                    color.clear()
                    for i in range(0, antnum):
                        pos = [random.randint(20, 620), random.randint(50, 620)]
                        ants = Ants(pos)
                        ant.append(ants)
                        color.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
                        #color.append((255, 255, 255))


    screen.fill([0,0,0])
    for i in range(0, interesnum):
        if (random.randint(0, 1000) == 666) and (interesnum > 1):
            interespointpos.pop(i)
            interesnum -= 1
    for i in range(0, interesnum):
        pygame.draw.circle(screen, (100, 0, 0), interespointpos[i], 20)
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
        path = []
        for j in range(0,interesnum):
            path.append(dist(ant[i].pos,interespointpos[j]))
        near = interespointpos[path.index(findmin(path))]
        nearestinterespoint = [near[0],near[1]]
        ant[i].steptoobj(nearestinterespoint)

        for j in range (0,antnum):
            if i!=j:
                if ((abs(ant[i].pos[0]-ant[j].pos[0])<size[0]) and (abs(ant[i].pos[1]-ant[j].pos[1])<size[1])):
                    ant[j].move(random.choice((-10,10)),random.choice((-10,10)))

        pygame.draw.rect(screen,color[i],r)

    pygame.display.flip()

pygame.quit()
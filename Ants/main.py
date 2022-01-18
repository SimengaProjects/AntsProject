import random
import pygame
import math

RUN = 1
WIDTH = 640
HEIGHT = 640
FPS = 30

antnum = 500
size = (3,3)

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


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
            gox = -2
        elif objpos[0] > self.pos[0] :
            gox = 2
        else:
            gox = 0;
        if objpos[1]<self.pos[1]:
            goy = -2
        elif objpos[1] > self.pos[1] :
            goy = 2
        else:
            goy = 0;
        self.move(gox,goy)

ant = []
color=[]

interespointpos = [320,320]

for i in range(0,antnum):
    pos = [random.randint(20,620) , random.randint(50,620)]
    ants = Ants(pos)
    ant.append(ants)
    color.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])


while RUN:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    interespointpos[0] = random.randint(10,630)
                    interespointpos[1] = random.randint(10, 630)
    screen.fill([0,0,0])
    for i in range(0,antnum):
        r = pygame.Rect(ant[i].pos[0], ant[i].pos[1],size[0],size[1])
        ant[i].steptoobj(interespointpos)
        for j in range (0,antnum):
            if i!=j:
                if ((abs(ant[i].pos[0]-ant[j].pos[0])<size[0]) and (abs(ant[i].pos[1]-ant[j].pos[1])<size[1])):
                    ant[j].move(random.choice((-10,10)),random.choice((-10,10)))
        pygame.draw.rect(screen,color[i],r)
    pygame.display.flip()

pygame.quit()
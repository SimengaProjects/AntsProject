import random
import time
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

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drow(self):
        pygame.draw.circle(screen, (180, 180, 180), (self.x, self.y), 3)

def create_new_Dot(rect,dots):
    point = random.choice(rect)
    new_Dot = Dot((point[0]+dots[-1].x)//2,(point[1]+dots[-1].y)//2)
    dots.append(new_Dot)

#Var's
if RUN:
    startTime = time.time()
    seconds = 0
    rect = []
    # first = [random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)]
    # second = [random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)]
    first = [WIDTH-70,HEIGHT-90]
    second = [120,60]
    rect.append([first[0],first[1]])
    rect.append([first[0], second[1]])
    rect.append([second[0], second[1]])
    rect.append([second[0], first[1]])
    first_Dot = Dot(random.randint(min(first[0],second[0]),max(first[0],second[0])),random.randint(min(first[1],second[1]),max(first[1],second[1])))
    dots = [first_Dot]



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

    pygame.draw.line(screen,(255,255,255),[first[0], first[1]],[first[0], second[1]])
    pygame.draw.line(screen, (255, 255, 255), [second[0], second[1]], [first[0], second[1]])
    pygame.draw.line(screen, (255, 255, 255), [second[0], first[1]], [second[0], second[1]])
    pygame.draw.line(screen, (255, 255, 255), [second[0], first[1]], [first[0], first[1]])

    for i in dots:
        i.drow()
    create_new_Dot(rect,dots)

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
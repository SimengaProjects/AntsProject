import pygame
import random

RUN = 1
WIDTH = 800
HEIGHT = 800
FPS = 30

#initialization of pygame
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

def findmin(a):
    min = a[0]
    for i in a:
        if i<min:
            min = i
    return min
def findmax(a):
    max = a[0]
    for i in a:
        if i>max:
            max = i
    return max
def findmaxindex(a):
    max = a[0]
    maxindex=[]
    for i in a:
        if i>max:
            max = i
    for i in range(0,len(a)):
        if a[i] == max:
            maxindex.append(i)

    return maxindex
def dist(first,second):
    return( round((((first[1]-second[1])**2+(first[0]-second[0])**2)**0.5)*100)/100 )

objCount = 0
objects = []

class Obj:
    def __init__(self,pos = [WIDTH/2,HEIGHT/2], type = 0,color = [255,255,255]):
        self.pos = pos
        self.type = type
        self.color = color
        self.speed = [0,0]
        self.rad = 3
    def drow(self):
        pygame.draw.circle(screen, self.color, self.pos, self.rad)
    def move(self):
        self.pos[0]+=self.speed[0]
        self.pos[1]+=self.speed[1]
    def steptoobj(self,obj):
        if self.pos[0]>obj[0]:
            x = 1
        else: x = -1
        if self.pos[1]>obj[1]:
            y = 1
        else: y = -1
        self.speed[0]-=x
        self.speed[1]-=y


for i in range (0,objCount):
    x = random.randint(50,WIDTH-50)
    y  = random.randint(50,HEIGHT-50)
    color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    pos = [x,y]
    newObject = Obj(pos,1,color)
    objects.append(newObject)
newObj = Obj()
newObj.type = -1
objCount+=1

while RUN:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                new = Obj(list(event.pos),1,[255,0,0])
                objects.append(new)
                objCount += 1
            if event.button == 2:
                new = Obj(list(event.pos), 1, [255, 0, 0])
                new.speed = [random.randint(0,30),random.randint(0,30)]
                objects.append(new)
                objCount += 1
            if event.button == 3:
                new = Obj(list(event.pos), -1, [0, 0, 255])
                objects.append(new)
                objCount+=1
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("___")
                if event.key == pygame.K_d:
                    print("d")
                if event.key == pygame.K_a:
                    print("a")
                    objCount = 0
                    objects.clear()

                if event.key == pygame.K_s:
                    print("InteresNum = ",' ')

                if event.key == pygame.K_w:
                    print("w")
                if event.key == pygame.K_g:
                    print("g")

    screen.fill([0,0,0])
    for i in objects:
        for j in objects:
            if j!=i:
                if j.type == -1 and i.type == 1:
                    i.steptoobj(j.pos)

    for o in objects:
        o.drow()
        o.move()
    pygame.display.flip()

pygame.quit()
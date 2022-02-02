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

objCount = 1
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

for i in range (0,objCount):
    x = random.randint(50,WIDTH-50)
    y = x = random.randint(50,HEIGHT-50)
    color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    pos = [x,y]
    newObject = Obj(pos,-random.choice([0,1,-1]),color)
    objects.append(newObject)


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
                new = Obj(list(event.pos),0, [0, 255, 0])
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
                    for i in objects:
                        i.type = random.choice([-1,0,1])
                        if i.type == 1:
                            i.color = [255,0,0]
                        if i.type == -1:
                            i.color = [0,255,0]
                        if i.type == 0:
                            i.color = [0,0,255]
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
        if i.pos[0]>WIDTH-50:
            i.pos[0] = WIDTH-50
        if i.pos[0]<50:
            i.pos[0] = 50
        if i.pos[1]>HEIGHT-50:
            i.pos[1] = HEIGHT-50
        if i.pos[1]<50:
            i.pos[1] = 50
        for j in objects:
            if i!=j and dist(i.pos,j.pos)>i.rad:
                if i.type == -1 and j.type==1:
                        i.speed[0] += -(i.pos[0]-j.pos[0])/(abs(i.pos[0]-j.pos[0])+1)/dist(i.pos,j.pos)*3
                        i.speed[1] += -(i.pos[1] - j.pos[1]) / (abs(i.pos[1] - j.pos[1])+1)/dist(i.pos,j.pos)*3
                if i.type == j.type != 0:
                        i.speed[0] += (i.pos[0]-j.pos[0])/((abs(i.pos[0]-j.pos[0]))+1)/dist(i.pos,j.pos)
                        i.speed[1] += (i.pos[1] - j.pos[1]) / ((abs(i.pos[1] - j.pos[1]))+1)/dist(i.pos,j.pos)
                if i.type == 1 and j.type == 0:
                    i.speed[0] += -(i.pos[0] - j.pos[0]) / ((abs(i.pos[0] - j.pos[0])) + 1) / (dist(i.pos, j.pos)) *1.1
                    i.speed[1] += -(i.pos[1] - j.pos[1]) / ((abs(i.pos[1] - j.pos[1])) + 1) / (dist(i.pos, j.pos)) *1.1
            if i != j and dist(i.pos, j.pos) < i.rad - 1:
                i.pos[0] += random.choice([i.rad,-i.rad])
                i.pos[1] += random.choice([i.rad, -i.rad])
                i.speed = [0,0]
            if i.speed[0]<-10:
                i.speed[0] = -10
            if i.speed[0]>10:
                i.speed[0] = 10
            if i.speed[1]<-10:
                i.speed[1] = -10
            if i.speed[1]>10:
                i.speed[1] = 10
    for i in objects:
        i.move()
        i.drow()
    pygame.display.flip()

pygame.quit()
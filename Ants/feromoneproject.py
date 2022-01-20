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


class Cell:
    def __init__(self,pos,fer = 0):
        self.pos = pos
        self.fer = fer
        self.color = (30,10,self.fer)
    def addfer(self,count):
        self.fer+=count
        if self.fer>51:
            self.fer = 51
        if self.fer<0:
            self.fer = 0
        self.color = (self.fer*5, 50, self.fer*5)

class Ant:
    def __init__(self,pos=[15,15]):
        self.pos = pos
    def check(self):

        print(a)



cells=[]

if RUN:
    ant = Ant([315,315])
    ant.check
    col = 0
    colon = 0
    cellnumx = WIDTH/30
    cellnumy = HEIGHT/30
    home = [random.randint(3,int(cellnumx)-3)*30+15,random.randint(3,int(cellnumy)-3)*30+15]
    for i in range(0,int(cellnumy)):
        for j in range(0,int(cellnumx)):
            if col == 50:
                colon=1
            if col == 0:
                colon = 0
            if colon == 0:
                col+=1
            else:
                col-=1
            cell = Cell([j*30,i*30])
            cell.addfer(col)
            cells.append(cell)

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
    for i in cells:
        r = pygame.Rect(i.pos,(30,30))
        pygame.draw.rect(screen, i.color, r,1)
    pygame.draw.circle(screen,(200,200,200),home[:],10)
    pygame.display.flip()

pygame.quit()
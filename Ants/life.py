import random
import pygame
import math

RUN = 1
WIDTH = 1024
HEIGHT = 800
FPS = 1

screensize = int(min(WIDTH,HEIGHT)/10)
generatorON = 1
antnum = 10
size = (3,3)
interesnum = 10
homefood = 0
gennum = 5
cell = []

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

class Cell:
    def __init__(self,x = 0, y = 0,life = 0):
        self.pos = [x,y]
        self.life = life
        self.color = [100,100,100]
        self.lifenear = 0
        self.nlife = -1
    def colorcheck(self):
        if self.life == 0:
            self.color = [255,255,255]
        else:
            self.color = [0,0,0]
    def drow(self):
        r = pygame.Rect(self.pos[0]*10, self.pos[1]*10,10,10)
        pygame.draw.rect(screen, self.color, r)
    def lifecheck(self):
        self.lifenear = 0
        for i in range (-1,1):
            for j in range (-1,1):
                if i!=j and self.pos[1]!=0 and self.pos[1]!=screensize and self.pos[0]!=0 and self.pos[0]!= screensize:
                    if cell[(self.pos[1]+i)*screensize+self.pos[0]+j].life == 1:
                        self.lifenear+=1
    def new(self):
        self.nlife = 0
        if self.lifenear == 1 and self.life == 1:
            self.nlife = 1
        #if self.lifenear == 2 and self.life == 1:
         #   self.nlife = 1
        if (self.lifenear == 3):
            self.nlife = 1
        if (self.lifenear == 2):
            self.nlife = 1
    def die(self):
        if self.nlife == 0:
            self.life = 0
        if self.nlife == 1:
            self.life = 1

for i in range(0,screensize):
    for j in range(0, screensize ):
        col = random.choice((0,0,0,0,1))
        newcell = Cell(j,i,col)
        cell.append(newcell)
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
                print("3")
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("___")
                if event.key == pygame.K_d:
                    print("d")
                if event.key == pygame.K_a:
                    print("a")

                if event.key == pygame.K_s:
                    print("InteresNum = ",' ')

                if event.key == pygame.K_w:
                    print("w")
                if event.key == pygame.K_g:
                    print("g")

    screen.fill([0,0,0])
    for c in cell:
        c.colorcheck()
        c.lifecheck()
        c.new()
    for c in cell:
        c.die()
        c.drow()
    pygame.display.flip()

pygame.quit()
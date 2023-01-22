import random
import time
import pygame as pg
import math

RUN = 1
WIDTH = 1280
HEIGHT = 690
FPS = 60
ticks = 0
secunds = 0

pg.init()
pg.mixer.init()  # для звука
screen = pg.display.set_mode((WIDTH, HEIGHT),pg.DOUBLEBUF)
pg.display.set_caption("My Game")
clock = pg.time.Clock()

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

class Interespoint:
    def __init__(self,pos,aimpoint = 1,rad = 25):
        self.pos = pos
        self.aimpoint = aimpoint
        self.rad = rad

    def drow(self):
        pg.draw.circle(screen,[255,0,0],self.pos,self.rad)




#Var's
if RUN:
    startTime = time.time()
    seconds = 0
    interesNum = 3
    for i in range(interesNum):
        pass



#Game cicle
while RUN:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(1)
            if event.button == 2:
                print(2)
            if event.button == 3:
                print(3)
        if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    print("d")
                if event.key == pg.K_a:
                    print("a")
                if event.key == pg.K_s:
                    print("InteresNum = ",' ')
                    print("AntNum = ", ' ')
                    print("Food in home = ", ' ')
                if event.key == pg.K_w:
                    print("w")
                if event.key == pg.K_g:
                    print("g")

    screen.fill([0,0,0])

    pg.draw.line(screen,(200,20,100),(40,40),(WIDTH-40,40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH-40, 40), (WIDTH - 40, HEIGHT-40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH-40, HEIGHT-40), (40, HEIGHT-40))
    pg.draw.line(screen, (200, 20, 100), (40, 40), ( 40, HEIGHT-40))
    pg.display.flip()
    t = time.time()
    if int(t-startTime) == seconds:
        seconds+=1


print("time: ",seconds-1)
pg.quit()
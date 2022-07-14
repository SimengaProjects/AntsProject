import random
import pygame as pg
import math
import time

RUN = 1
WIDTH = 1280
HEIGHT = 950
FPS = 60
ticks = 0
secunds = 0
GRAPH = [[0,0]]

pg.init()
pg.mixer.init()  # для звука
screen = pg.display.set_mode((WIDTH, HEIGHT),pg.DOUBLEBUF,1)
scr = pg.display.set_mode((WIDTH, HEIGHT),pg.DOUBLEBUF,1)
pg.display.set_caption("My Game")
clock = pg.time.Clock()

screen.set_alpha(None)

##ToDO:
#add +Home+ and food-eating sistems, add Quin and +aim's changing+.

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

#Var's
if RUN:
    poses = [[0.1,0.001],[0.7,0.635],[0.666,0.111],[0.433,0.1],[0.125,0.979,],[0.12,0.3],[0.5,0.555],[0.9,0.12],[0.553,0.666],[0.1,0.221]]
    p1 = [0, 0.923]
    p2 = [0.912, 0]
    p1[0]+=40
    p2[1]+=40
    p1[1]*=HEIGHT
    p2[0]*=WIDTH
    cos = findcos(p1,p2)

pg.event.set_allowed([pg.QUIT, pg.KEYDOWN, pg.MOUSEBUTTONDOWN])
scr.fill([0, 0, 0])
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
    pg.draw.line(screen,(255,255,255),(0*WIDTH,HEIGHT),(1*WIDTH,0))
    for i in poses:
        pg.draw.circle(screen,(255,255,0),[i[0]*WIDTH,HEIGHT-i[1]*HEIGHT],5)



    pg.draw.line(screen,(200,20,100),(40,40),(WIDTH-40,40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH-40, 40), (WIDTH - 40, HEIGHT-40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH-40, HEIGHT-40), (40, HEIGHT-40))
    pg.draw.line(screen, (200, 20, 100), (40, 40), ( 40, HEIGHT-40))
    pg.display.flip()
    ticks+=1
    if ticks == FPS/2:
        secunds+=0.5
        ticks = 0


print("time: ",secunds)

pg.quit()
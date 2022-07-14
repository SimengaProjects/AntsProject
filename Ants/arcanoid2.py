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


class board():
    def __init__(self,width = 150,pos=WIDTH/2,speed = 8):
        self.width = width
        self.pos = pos
        self.speed = speed

    def move(self,nav):
        self.pos+=self.speed*nav
        if self.pos>WIDTH-50-self.width:
            self.pos = WIDTH-50-self.width
        if self.pos<50:
            self.pos = 50
    def drow(self):
        pg.draw.rect(screen,(150,0,255),(self.pos, HEIGHT-70, self.width, 10))

class ball():
    def __init__(self,rad=10,pos=[WIDTH/2+75,HEIGHT-80],speed=10,nav = 0.82,color = [255,255,255]):
        self.rad = rad
        self.pos = pos
        self.speed = speed
        self.color = color
        self.nav = nav
        self.ymod = -1
    def move(self,change):
        self.pos[0]+=change[0]
        self.pos[1] += change[1]
        if self.pos[0]>WIDTH-100-self.rad:
            self.pos[0] = WIDTH-100-self.rad
        if self.pos[0]<125:
            self.pos[0] = 125
    def drow(self):
        pg.draw.circle(screen,self.color,self.pos,self.rad)
    def movetonav(self):
        self.pos[0] += self.nav * self.speed
        self.pos[1] += (1 - (self.nav) ** 2) ** 0.5 * self.speed * self.ymod
    def fizmove(self):
        self.movetonav()
        if self.pos[0]<50 or self.pos[0]>WIDTH-50:
            self.nav*=-1
        if self.pos[1]<50:
            self.pos[1] = 50
            self.ymod*=-1;

class Block:
    def __init__(self,pos,life = 1,size = [100,40],color = [50,200,50]):
        self.pos = pos
        self.life = life
        self.size = size
        self.color = color
        self.rect = pg.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
    def drow(self):
        pg.draw.rect(screen,self.color,self.rect)

def ballblock(block,ball):
    if ball.pos[0]>block.pos[0] and ball.pos[0]<block.pos[0]+block.size[0]:
        if (ball.pos[1]+ball.rad > block.pos[1] and ball.pos[1]<block.pos[1]) or (ball.pos[1]-ball.rad < block.pos[1]+block.size[1] and ball.pos[1]>block.pos[1]+block.size[1]):
            ball.ymod *= -1
            return 1
    if ball.pos[1]<block.pos[1] and ball.pos[1]>block.pos[1]+block.size[1]:
        if (ball.pos[0]<block.pos[0] and ball.pos[0]+ball.rad > block.pos[0]) or (ball.pos[0]>block.pos[0]+block.size[1] and ball.pos[0]-ball.rad < block.pos[0]+block.size[0]):
            ball.nav *= -1
            return 1

def blockcheck(bgroup,ball):
    for i in bgroup:
        if ballblock(i,ball):
            bgroup.remove(i)

#Var's
if RUN:
    startTime = time.time()
    seconds = 0
    stop = 1
    move = 0

    player = board()
    mainball = ball()

    blocknum = 60
    blocks = []
    bx = 100
    by = 100
    for i in range(blocknum):
        if bx>WIDTH-150:
            bx = 100
            by += 50
        newblock = Block([bx,by])
        blocks.append(newblock)
        bx+=105

#Game cicle
while RUN:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                stop = 0
                print(1)
            if event.button == 2:
                print(2)
            if event.button == 3:
                print(3)
        if event.type == pg.KEYUP:
            if event.key == pg.K_d:
                move = 0
            if event.key == pg.K_a:
                move = 0
        if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    print("d")
                    move = 1
                if event.key == pg.K_a:
                    print("a")
                    move = -1
                if event.key == pg.K_s:
                    print("InteresNum = ",' ')
                    print("AntNum = ", ' ')
                    print("Food in home = ", ' ')
                if event.key == pg.K_w:
                    print("w")
                if event.key == pg.K_g:
                    print("g")

    #drow
    screen.fill([0,0,0])
    player.drow()
    mainball.drow()
    for i in blocks:
        i.drow()
    blockcheck(blocks,mainball)

    ##  Mooooooooving
    player.move(move)
    if stop:
        mainball.move([player.speed * move, 0])
        mainball.nav = -1 + 2*(mainball.pos[0]/WIDTH)
    else:
        mainball.fizmove()

    if mainball.pos[1]>HEIGHT-80+mainball.rad and mainball.pos[1]<HEIGHT-60+mainball.rad and mainball.pos[0]>player.pos and mainball.pos[0]<player.pos + player.width:
        mainball.ymod*=-1

    ##Loose
    if mainball.pos[1]>HEIGHT-50:
        stop = 1
        mainball.pos[0] = player.pos+player.width/2
        mainball.pos[1] = HEIGHT-( 70+mainball.rad)
        mainball.ymod = -1

    ##WIN
    if not (blocks):
        print("You WIN!")
        stop = 1
        RUN = 0
    #board
    pg.draw.line(screen,(200,20,100),(40,40),(WIDTH-40,40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH-40, 40), (WIDTH - 40, HEIGHT-40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH-40, HEIGHT-40), (40, HEIGHT-40))
    pg.draw.line(screen, (200, 20, 100), (40, 40), ( 40, HEIGHT-40))
    pg.display.flip()
    t = time.time()
    if int(t-startTime) >= seconds:
        seconds+=1


print("time: ",seconds-1)
pg.quit()
import random
import pygame as pg
import math
import time

# Change side and up mechanic


RUN = 1
WIDTH = 1280
HEIGHT = 720
FPS = 60
ticks = 0
secunds = 0

FireBall = 0

pg.init()
pg.mixer.init()  # для звука
screen = pg.display.set_mode((WIDTH, HEIGHT),pg.DOUBLEBUF,1)
pg.display.set_caption("My Game")
clock = pg.time.Clock()

screen.set_alpha(None)


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

class Hero:
    def __init__(self,wid = 150,x = (WIDTH)/2):
        self.x = x
        self.wid = wid
        self.speed = 5
    def move(self,nav):
        self.x+=self.speed*nav
        if self.x>WIDTH-50-self.wid:
            self.x = WIDTH-50-self.wid
        if self.x<50:
            self.x = 50
    def drow(self):
        pg.draw.rect(screen,(150,0,255),(self.x, HEIGHT-70, self.wid, 10))


class Obj:
    def __init__(self,pos = [WIDTH/2,HEIGHT/2],color = [255,255,255],rad = 10,speed = 1):
        self.pos = pos
        self.speed = speed
        self.ymod = 1
        self.nav = random.randint(-1000,1000)/1000
        self.rad = rad
        self.color = color
    def move(self,change):
        self.pos[0]+=change[0]
        self.pos[1] += change[1]
    def randstep(self):
        self.pos[0] += random.choice([-1, 0, 1])
        self.pos[1] += random.choice([-1, 0, 1])
    def drow(self):
        pg.draw.circle(screen,self.color,self.pos,self.rad)
    def randnavchange(self):
        self.nav += random.randint(-3000,3000)/30000
        if self.nav>1:
            self.nav = 1
        if self.nav <-1:
            self.nav = -1
        if self.nav == 1 or self.nav == -1:
            self.ymod = -self.ymod
    def movetonav(self):
        self.pos[0] += self.nav * self.speed
        self.pos[1] += (1 - (self.nav) ** 2) ** 0.5 * self.speed * self.ymod

class block:
    def __init__(self,pos,life = 1,size = [100,20]):
        self.pos = pos
        self.life = life
        self.color = [50,150,80]
        self.color1 = [100,220,130]
        self.size = size
    def drow(self):
        pg.draw.rect(screen,self.color,(self.pos[0],self.pos[1], self.size[0],self.size[1]))
        pg.draw.rect(screen, self.color1, (self.pos[0]-1, self.pos[1]-2, self.size[0]+1, self.size[1]+2),2)

def blocker(object,group):
    for i in group:
        if object.pos[0]>i.pos[0] and object.pos[0]<i.pos[0]+i.size[0] and object.pos[1]>i.pos[1] and object.pos[1]<i.pos[1]+i.size[1]:
            group.remove(i)
            if FireBall == 0:
                object.ymod*=-1
                if abs(object.nav)>0.9:
                    object.ymod *= -1
                    object.nav=-object.nav


#Var's
if RUN:
    move = 0
    blocks = []
    h = Hero()
    ball = Obj([h.x+h.wid/2,HEIGHT-81])
    ball.speed = 3
    ballmove = 0
    b = block([600,200])
    for i in range(8):
        for j in range(10):
            newb = block([200+j*80,100+i*50],1,[70,30])
            blocks.append(newb)


#Game cicle
while RUN:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(1)
                ballmove = 1
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
                    h.move(1)
                if event.key == pg.K_a:
                    print("a")
                    move = -1
                    h.move(-1)
                if event.key == pg.K_s:
                    h.speed -= 1
                    ball.speed -= 1
                if event.key == pg.K_w:
                    print("w")
                    ball.speed+=1
                    h.speed+=1
                if event.key == pg.K_r:
                    print("r")
                    ball.speed*=-1
    screen.fill([0,0,0])

    if move == 1:
        h.move(1)
    if move == -1:
        h.move(-1)

    if ball.pos[0] < 50 or ball.pos[0] > WIDTH - 50:
        ball.nav = -ball.nav
    if ball.pos[1] < 50:
        ball.ymod = -ball.ymod
    if ball.pos[0]>h.x and ball.pos[0]<h.x+h.wid and ball.pos[1]>HEIGHT-80 and ball.pos[1]<HEIGHT-50:
        ball.ymod = -ball.ymod
        ball.nav = ((ball.pos[0]-h.x)/h.wid) * 2 - 1
    if ball.pos[1]>HEIGHT-10:
        ballmove = 0
        ball.ymod = -1
    if ballmove:
        ball.movetonav()
    if ballmove == 0:
        ball.pos = [h.x+h.wid/2,HEIGHT-81]
        ball.nav = -1 + (h.x/WIDTH)*2

    blocker(ball,blocks)

    h.drow()
    ball.drow()
    for i in blocks:
        i.drow()
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
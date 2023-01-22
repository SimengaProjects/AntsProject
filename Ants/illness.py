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
GRAPH = [[0, 0]]

pg.init()
pg.mixer.init()  # для звука
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.DOUBLEBUF, 1)
scr = pg.display.set_mode((WIDTH, HEIGHT), pg.DOUBLEBUF, 1)
pg.display.set_caption("My Game")
clock = pg.time.Clock()

screen.set_alpha(None)


##ToDO:
# add +Home+ and food-eating sistems, add Quin and +aim's changing+.

def findmin(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    return min


def scalarmult(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def findcos(v1, v2):
    mult = scalarmult(v1, v2)
    len1 = (v1[0] ** 2 + v1[1] ** 2) ** 0.5
    len2 = (v2[0] ** 2 + v2[1] ** 2) ** 0.5
    return (mult / (len1 * len2))


def dist(first, second):
    return (round((((first[1] - second[1]) ** 2 + (first[0] - second[0]) ** 2) ** 0.5) * 100) / 100)


class Man:
    def __init__(self, pos=[WIDTH / 2, HEIGHT / 2], protection=0, ill=0, speed=1):
        self.pos = pos
        self.ill = ill
        self.prot = protection
        self.speed = speed
        self.ymod = random.choice([-1, 1])
        self.nav = random.randint(-1000, 1000) / 1000
        if self.ill == 0:
            self.color = [0, protection * 2, 100 - protection]
        else:
            self.color = [200, 10, 10]

    def move(self, change):
        self.pos[0] += change[0]
        self.pos[1] += change[1]

    def randstep(self):
        self.pos[0] += random.choice([-1, 0, 1])
        self.pos[1] += random.choice([-1, 0, 1])

    def cough(self, humanity, coughrange=30):
        if self.ill == 1:
            pg.draw.circle(screen, (100, 100, 10), self.pos, coughrange)
            self.drow()
        for i in humanity:
            if (self.ill == 1 and i.ill == 0 and dist(self.pos, i.pos) < coughrange and self != i and random.randint(0,
                                                                                                                     100) > i.prot):
                i.color = [200, 10, 10];
                i.ill = 1

    def drow(self):
        pg.draw.circle(screen, self.color, self.pos, 3)

    def randnavchange(self):
        self.nav += random.randint(-3000, 3000) / 30000
        if self.nav > 1:
            self.nav = 1
        if self.nav < -1:
            self.nav = -1
        if self.nav == 1 or self.nav == -1:
            self.ymod = -self.ymod

    def movetonav(self):
        self.pos[0] += self.nav * self.speed
        self.pos[1] += (1 - (self.nav) ** 2) ** 0.5 * self.speed * self.ymod

    def illcheck(self):
        if self.ill == 1:
            return 1


# Var's
if RUN:
    ztime = time.time()
    hums = []
    hnum = 1000
    for i in range(hnum):
        man = Man([random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)], random.randint(0, 95), 0)
        hums.append(man)
    man = Man([random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)], 0, 1)
    hums.append(man)

pg.event.set_allowed([pg.QUIT, pg.KEYDOWN, pg.MOUSEBUTTONDOWN])
scr.fill([0, 0, 0])
# Game cicle
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
                print("InteresNum = ", ' ')
                print("AntNum = ", ' ')
                print("Food in home = ", ' ')
            if event.key == pg.K_w:
                print("w")
            if event.key == pg.K_g:
                print("g")
    for i in GRAPH:
        pg.draw.circle(scr, [255, 0, 0], [i[0] * 10 + 100, -i[1] + (HEIGHT - 50)], 3)
    pg.display.flip()
    screen.fill([0, 0, 0])

    for i in hums:
        i.movetonav()
        i.randnavchange()
        i.drow()
        if random.randint(0, 100) == 66:
            i.cough(hums, 20)
        if i.pos[0] < 50 or i.pos[0] > WIDTH - 50:
            i.nav = -i.nav
        if i.pos[1] < 50 or i.pos[1] > HEIGHT - 50:
            i.ymod = -i.ymod

    pg.draw.line(screen, (200, 20, 100), (40, 40), (WIDTH - 40, 40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH - 40, 40), (WIDTH - 40, HEIGHT - 40))
    pg.draw.line(screen, (200, 20, 100), (WIDTH - 40, HEIGHT - 40), (40, HEIGHT - 40))
    pg.draw.line(screen, (200, 20, 100), (40, 40), (40, HEIGHT - 40))
    pg.display.flip()
    ticks += 1
    if ticks == FPS / 2:
        secunds += 0.5
        ticks = 0
        t = round(time.time() - ztime, 2)
        illnum = 0
        for i in hums:
            if i.ill == 1:
                illnum += 1
        GRAPH.append([t, illnum])

print("time: ", secunds)

RUN = 1
scr.fill([0, 0, 0])
while RUN:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            RUN = False
    for i in GRAPH:
        pg.draw.circle(scr, [255, 0, 0], [i[0] * 10 + 100, -i[1] + (HEIGHT - 50)], 3)
    pg.display.flip()
pg.quit()
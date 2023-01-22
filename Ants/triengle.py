import random
import time
import pygame
import math

# Const
RUN = 1
RandomTriengle = 1
WIDTH = 1280
HEIGHT = 690
FPS = 60
ticks = 0
secunds = 0

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

screen.set_alpha(None)


##ToDO: Ready

# Some math def's
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

#class zone
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drow(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 1)


def generate_new_dot(triengle):
    newDot = Dot(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
    x1 = triengle[0][0]
    x2 = triengle[1][0]
    x3 = triengle[2][0]
    y1 = triengle[0][1]
    y2 = triengle[1][1]
    y3 = triengle[2][1]
    x0 = newDot.x
    y0 = newDot.y
    if (((x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)) > 0 and (
            (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)) > 0 and (
                (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)) > 0) or (
            ((x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)) < 0 and (
            (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)) < 0 and ((x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)) < 0):
        return newDot
    else:
        return 0

def create_new_Dot(triengle,dots):
    point = random.choice(triengle)
    new_Dot = Dot((point[0]+dots[-1].x)//2,(point[1]+dots[-1].y)//2)
    dots.append(new_Dot)

# Var's and conditions
if RUN:
    startTime = time.time()
    seconds = 0
    if RandomTriengle:
        triengle = []
        for i in range(3):
            newDot = (random.randint(50, WIDTH), random.randint(50, HEIGHT))
            triengle.append(newDot)
    else:
        triengle =[[WIDTH/2,70],[WIDTH-100,HEIGHT-100],[140,HEIGHT-200]]
    first_Dot = 0
    while not(first_Dot):
        first_Dot = generate_new_dot(triengle)
    dots = [first_Dot]

# Drow cicle
while RUN:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(1)
                print(len(dots))
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
                print("InteresNum = ", ' ')
                print("AntNum = ", ' ')
                print("Food in home = ", ' ')
            if event.key == pygame.K_w:
                print("w")
            if event.key == pygame.K_g:
                print("g")

    screen.fill([0, 0, 0])
    for i in triengle:
        for j in triengle:
            pygame.draw.line(screen,(255,255,255),[i[0],i[1]],[j[0],j[1]])
    for i in dots:
        i.drow()
    create_new_Dot(triengle,dots)

    pygame.draw.line(screen, (200, 20, 100), (40, 40), (WIDTH - 40, 40))
    pygame.draw.line(screen, (200, 20, 100), (WIDTH - 40, 40), (WIDTH - 40, HEIGHT - 40))
    pygame.draw.line(screen, (200, 20, 100), (WIDTH - 40, HEIGHT - 40), (40, HEIGHT - 40))
    pygame.draw.line(screen, (200, 20, 100), (40, 40), (40, HEIGHT - 40))
    pygame.display.flip()
    t = time.time()
    if int(t - startTime) == seconds:
        seconds += 1

print("time: ", seconds - 1)
pygame.quit()

import random
import time
import pygame
import math

RUN = 1
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


##ToDO:


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


class Circle:
    def __init__(self, *args, **kwargs):
        self.pos = kwargs['posititon']
        self.type = kwargs['type']
        self.speed = kwargs['speed']

    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

    def drow(self):
        if self.type == 1:
            color = (255, 0, 0)
        elif self.type == 0:
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)

        pygame.draw.circle(screen, color, self.pos, 3)


# Var's
if RUN:
    startTime = time.time()
    seconds = 0
    circle_count = 0
    circles = []
    for i in range(circle_count):
        newCircle = Circle(posititon=[random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)], speed=[0, 0],
                           type=random.randint(-1, 1))
        circles.append((newCircle))

# Game cicle
while RUN:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(1)
                newCircle = Circle(posititon=list(event.pos), speed=[0, 0], type=1)
                circles.append((newCircle))
            if event.button == 2:
                print(2)
                newCircle = Circle(posititon=list(event.pos), speed=[0, 0], type=0)
                circles.append((newCircle))
            if event.button == 3:
                print(3)
                newCircle = Circle(posititon=list(event.pos), speed=[0, 0], type=-1)
                circles.append((newCircle))
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

    for circle in circles:
        circle.drow()
        for scircle in circles:
            if not (circle is scircle):
                if (circle.type == -1 and scircle == 1) or (circle.type == 1 and scircle.type == -1) or (
                        circle.type == 1 and scircle.type == 0) or (circle.type == 0 and scircle.type == 1) or (
                        circle.type == 1 and scircle == 1):
                    try:
                        horisontal =  WIDTH / ((circle.pos[0] - scircle.pos[0]) * 50)
                        if horisontal > 1:
                            horisontal = 1
                        elif horisontal < -1:
                            horisontal = -1
                        vertical =  HEIGHT / ((circle.pos[1] - scircle.pos[1]) * 50)
                        if vertical > 1:
                            vertical = 1
                        elif vertical < -1:
                            vertical = -1
                        circle.speed[0] -= horisontal
                        circle.speed[1] -= vertical
                    except ZeroDivisionError:
                        pass

            if (circle.type == scircle.type and circle.type != 0):
                    try:
                        horisontal = WIDTH / ((circle.pos[0] - scircle.pos[0]) * 1000)
                        if horisontal > 1:
                            horisontal = 1
                        elif horisontal < -1:
                            horisontal = -1
                        vertical = HEIGHT / ((circle.pos[1] - scircle.pos[1]) * 1000)
                        if vertical > 1:
                            vertical = 1
                        elif vertical < -1:
                            vertical = -1
                        circle.speed[0] += horisontal
                        circle.speed[1] += vertical
                    except ZeroDivisionError:
                        pass
            if circle.speed[0] > 10:
                circle.speed[0] = 10
            elif circle.speed[0] < -10:
                circle.speed[0] = -10
            if circle.speed[1] > 10:
                circle.speed[1] = 10
            elif circle.speed[1] < -10:
                circle.speed[1] = -10
            circle.move()

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

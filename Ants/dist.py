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
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.DOUBLEBUF)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

screen.set_alpha(None)



#Var's
if RUN:
    startTime = time.time()
    seconds = 0
    Coef = 1.9
    rad = 75
    dot = [WIDTH/2,HEIGHT/2]
    dots = []
    for i in range(int(WIDTH/2)-100,int(WIDTH/2)+100):
        for j in range(int(HEIGHT/2) - 100, int(HEIGHT/2) + 100):
            if abs(abs(dot[0]-i)+abs(dot[1]-j)) / Coef < rad :
                dots.append([i,j])



#Game cicle
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
                if event.key == pygame.K_d:
                    print("d")
                if event.key == pygame.K_a:
                    print("a")
                if event.key == pygame.K_s:
                    print("InteresNum = ",' ')
                    print("AntNum = ", ' ')
                    print("Food in home = ", ' ')
                if event.key == pygame.K_w:
                    print("w")
                if event.key == pygame.K_g:
                    print("g")

    screen.fill([0,0,0])

    pygame.draw.circle(screen, (255, 0, 0), (WIDTH / 2, HEIGHT / 2),105)
    for i in dots:
        pygame.draw.circle(screen,(255,255,255),i,3)

    pygame.draw.line(screen,(200,20,100),(40,40),(WIDTH-40,40))
    pygame.draw.line(screen, (200, 20, 100), (WIDTH-40, 40), (WIDTH - 40, HEIGHT-40))
    pygame.draw.line(screen, (200, 20, 100), (WIDTH-40, HEIGHT-40), (40, HEIGHT-40))
    pygame.draw.line(screen, (200, 20, 100), (40, 40), ( 40, HEIGHT-40))
    pygame.display.flip()
    t = time.time()
    if int(t-startTime) == seconds:
        seconds+=1


print("time: ",seconds-1)
pygame.quit()
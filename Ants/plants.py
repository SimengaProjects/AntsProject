import random
import pygame
import math

RUN = 1
WIDTH = 1024
HEIGHT = 800
FPS = 144

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

    pygame.display.flip()

pygame.quit()
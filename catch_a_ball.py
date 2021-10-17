import pygame
from pygame.draw import *
from random import randint
from random import random
pygame.init()
pygame.font.init()

FPS = 60
number1 = 10
object_number = 10
screen = pygame.display.set_mode((1500, 1000))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball(k):
    circle(screen, color[k], (x1[k], y1[k]), r1[k])


def is_hit(x_mouse, y_mouse, k):
    if (x1[k] - x_mouse)**2 + (y1[k] - y_mouse)**2 <= r1[k]**2:
        return True
    else:
        return False

def point_draw():
    font1 = pygame.font.SysFont('arial', 100)
    text = str(points1)
    tekst = font1.render(text, True, WHITE)
    screen.blit(tekst, (10, 10))

clock = pygame.time.Clock()
finished = False

im1 = pygame.image.load('9_purple.png')

a = 0
b = 0
points1 = 0
points2 = 0
hitreg = [0]*number1
x1 = [750]*number1
y1 = [500]*number1
r1 = [50]*number1
Vx1 = [0]*number1
Vy1 = [0]*number1
color = [COLORS[randint(0, 5)]]*number1
new_ball(1)
pygame.display.update()

for i in range(number1):
    x1[i] = randint(100, 1400)
    y1[i] = randint(100, 900)
    r1[i] = randint(20, 80)
    Vx1[i] = ((random()-0.5)/0.5)*10
    Vy1[i] = ((random()-0.5)/0.5)*10
    color[i] = COLORS[randint(0, 5)]

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                a = event.pos[0]
                b = event.pos[1]

    for i in range(number1):
        if x1[i] <= r1[i] or x1[i] >= 1500 - r1[i]: Vx1[i] = -Vx1[i]
        if y1[i] <= r1[i] or y1[i] >= 1000 - r1[i]: Vy1[i] = -Vy1[i]

    for i in range(number1):
        new_ball(i)
        x1[i] += Vx1[i]
        y1[i] += Vy1[i]

    screen.fill(BLACK)

    for i in range(number1):
        new_ball(i)

    for i in range(number1):
        if is_hit(a, b, i):
            hitreg[i] = 1
        else: hitreg[i] = 0

    for i in range(number1):
        if hitreg[i] == 1:
            x1[i] = randint(100, 1400)
            y1[i] = randint(100, 900)
            r1[i] = randint(20, 80)
            Vx1[i] = ((random()-0.5)/0.5)*10
            Vy1[i] = ((random()-0.5)/0.5)*10
            color[i] = COLORS[randint(0, 5)]
            points1 += 1
            new_ball(i)
            screen.fill(BLACK)
            pygame.display.update()

    point_draw()
    a = 0
    b = 0
    pygame.display.update()

pygame.quit()
pygame.font.quit()
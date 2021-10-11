import pygame
from pygame.draw import *
from random import randint
from random import random
pygame.init()
pygame.font.init()

FPS = 60
number = 20
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
    circle(screen, color[k], (x[k], y[k]), r[k])


def is_hit(x_mouse, y_mouse, k):
    if (x[k] - x_mouse)**2 + (y[k] - y_mouse)**2 <= r[k]**2:
        return True
    else:
        return False

def point_draw():
    font1 = pygame.font.SysFont('arial', 100)
    text = str(points)
    tekst = font1.render(text, True, WHITE)
    screen.blit(tekst, (10, 10))

clock = pygame.time.Clock()
finished = False

a = 0
b = 0
points = 0
hitreg = [0]*number
x = [750]*number
y = [500]*number
r = [50]*number
Vx = [0]*number
Vy = [0]*number
color = [COLORS[randint(0, 5)]]*number
new_ball(1)
pygame.display.update()

for i in range(number):
    x[i] = randint(100, 1400)
    y[i] = randint(100, 900)
    r[i] = randint(20, 80)
    Vx[i] = ((random()-0.5)/0.5)*10
    Vy[i] = ((random()-0.5)/0.5)*10
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

    for i in range(number):
        if x[i] <= r[i] or x[i] >= 1500 - r[i]: Vx[i] = -Vx[i]
        if y[i] <= r[i] or y[i] >= 1000 - r[i]: Vy[i] = -Vy[i]

    for i in range(number):
        new_ball(i)
        x[i] += Vx[i]
        y[i] += Vy[i]

    screen.fill(BLACK)

    for i in range(number):
        new_ball(i)

    for i in range(number):
        if is_hit(a, b, i):
            hitreg[i] = 1
        else: hitreg[i] = 0

    for i in range(number):
        if hitreg[i] == 1:
            x[i] = randint(100, 1400)
            y[i] = randint(100, 900)
            r[i] = randint(20, 80)
            Vx[i] = ((random()-0.5)/0.5)*10
            Vy[i] = ((random()-0.5)/0.5)*10
            color[i] = COLORS[randint(0, 5)]
            points += 1
            new_ball(i)
            screen.fill(BLACK)
            pygame.display.update()

    point_draw()
    print(x, y, r)
    print(a, b)
    #print((x - a)**2 + (y - b)**2 <= r**2)
    #print(is_hit(a, b))
    a = 0
    b = 0
    pygame.display.update()

pygame.quit()
pygame.font.quit()
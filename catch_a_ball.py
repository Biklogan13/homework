import pygame
from pygame.draw import *
from random import randint
from random import random
pygame.init()
pygame.font.init()

FPS = 60
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

def new_ball(color):
    circle(screen, color, (x, y), r)


def is_hit(x_mouse, y_mouse):
    if (x - x_mouse)**2 + (y - y_mouse)**2 <= r**2:
        return True
    else:
        return False

def point_draw():
    global points
    font1 = pygame.font.SysFont('arial', 100)
    text = str(points)
    tekst = font1.render(text, True, WHITE)
    screen.blit(tekst, (10, 10))

clock = pygame.time.Clock()
finished = False


a = 0
b = 0
points = 0
x = 750
y = 500
r = 50
Vx = 0
Vy = 0
color = COLORS[randint(0, 5)]
new_ball(color)
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                a = event.pos[0]
                b = event.pos[1]

    if x <= r or x >= 1500-r: Vx = -Vx
    if y <= r or y >= 1000-r: Vy = -Vy

    new_ball(color)
    x += Vx
    y += Vy
    screen.fill(BLACK)
    new_ball(color)

    if is_hit(a, b):
        x = randint(100, 1100)
        y = randint(100, 900)
        r = randint(10, 100)
        Vx = ((random()-0.5)/0.5)*10
        Vy = ((random()-0.5)/0.5)*10
        color = COLORS[randint(0, 5)]
        points += 1
        new_ball(color)
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
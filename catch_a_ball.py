import pygame
from pygame.draw import *
from random import randint
from random import random
pygame.init()
pygame.font.init()

FPS = 60
number1 = 20
screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

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
    font1 = pygame.font.SysFont('arial', int(100*screen_height/1500))
    text = str(points)
    tekst = font1.render(text, True, WHITE)
    screen.blit(tekst, (10, 10))

clock = pygame.time.Clock()
finished = False

im1 = pygame.image.load('9_purple.png')
a = 0
b = 0
points = 0
hitreg = [0]*number1
x1 = [0]*number1
y1 = [0]*number1
r1 = [0]*number1
Vx1 = [0]*number1
Vy1 = [0]*number1
x2 = 0
y2 = screen_height
Vy2 = 5
sus_finished = 0
color = [COLORS[randint(0, 5)]]*number1

for i in range(number1):
    x1[i] = randint(100, screen_width - 100)
    y1[i] = randint(100, screen_height - 100)
    r1[i] = randint(20, 80)
    Vx1[i] = ((random()-0.5)/0.5)*10
    Vy1[i] = ((random()-0.5)/0.5)*10
    color[i] = COLORS[randint(0, 5)]

x2 = randint(0, screen_width - 150)

font2 = pygame.font.SysFont('arial', int(100*screen_height/1500))
tekst = font2.render('Enter nickname', True, WHITE)
screen.blit(tekst, (10, 10))
pygame.display.update()

print("Enter nickname")
nick = input()

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
        if x1[i] <= r1[i] or x1[i] >= screen_width - r1[i]: Vx1[i] = -Vx1[i]
        if y1[i] <= r1[i] or y1[i] >= screen_height - r1[i]: Vy1[i] = -Vy1[i]

    if y2 <= screen_height - 150:
        Vy2 = -Vy2
    elif y2 >= screen_height + 100:
        Vy2 = -Vy2
        sus_finished = 1

    screen.blit(im1, (x2, y2))
    y2 += Vy2

    for i in range(number1):
        new_ball(i)
        x1[i] += Vx1[i]
        y1[i] += Vy1[i]

    screen.fill(BLACK)

    screen.blit(im1, (x2, y2))

    for i in range(number1):
        new_ball(i)

    for i in range(number1):
        if is_hit(a, b, i):
            hitreg[i] = 1
        else: hitreg[i] = 0

    for i in range(number1):
        if hitreg[i] == 1:
            x1[i] = randint(100, screen_width - 100)
            y1[i] = randint(100, screen_height - 100)
            r1[i] = randint(20, 80)
            Vx1[i] = ((random()-0.5)/0.5)*10
            Vy1[i] = ((random()-0.5)/0.5)*10
            color[i] = COLORS[randint(0, 5)]
            points += 1
            new_ball(i)
            screen.fill(BLACK)
            pygame.display.update()

    if a >= x2 and a <= x2 + 150 and b >= y2 and b <= y2 + 200: points += 10

    if sus_finished == 1:
        x2 = randint(0, screen_width - 150)
        sus_finished = 0

    point_draw()
    a = 0
    b = 0
    pygame.display.update()

text = open('recordtable.txt', 'r')
table = text.readlines()

linenum = len(table)
best_scores = [0]*5
best_scores_numbers = [0]*6
best_scores_names = [0]*6
sort_trigger = 0

best_scores_numbers[5] = points
best_scores_names[5] = nick

for i in range(5):
    best_scores[i] = table[i].split()

for i in range(5):
    best_scores_numbers[i] = int(best_scores[i][0])
    best_scores_names[i] = best_scores[i][1]

for i in range(5):
    if points > best_scores_numbers[i]:
        sort_trigger = 1

temp = 0

if sort_trigger == 1:
    for i in range(6):
        for k in range(i):
            if best_scores_numbers[k] < best_scores_numbers[i]:
                temp = best_scores_numbers[i]
                best_scores_numbers[i] = best_scores_numbers[k]
                best_scores_numbers[k] = temp
                temp = best_scores_names[i]
                best_scores_names[i] = best_scores_names[k]
                best_scores_names[k] = temp

best = open('recordtable.txt', 'w')
for i in range(5):
    print(best_scores_numbers[i], best_scores_names[i], file=best)

for i in range(5):
    print(best_scores_numbers[i], best_scores_names[i])

print('Your score:', points)
best.close()
text.close()
pygame.quit()
pygame.font.quit()
import math
from random import choice
import random
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLACK, RED, GREEN]

WIDTH = 1500
HEIGHT = 1000


class Ball:
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = 20 + math.cos(gun.an)*gun.f2_power
        self.y = 450 + math.sin(gun.an)*gun.f2_power
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """

        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.pos[1]-(HEIGHT/2)), (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        #y = 450, x = 20
        pygame.draw.line(self.screen, self.color, (20, (HEIGHT/2)), (20 + math.cos(self.an)*self.f2_power, (HEIGHT/2) + math.sin(self.an)*self.f2_power), width=10)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 5
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.x = random.randint(WIDTH - 200, WIDTH - 61)
        self.y = random.randint(HEIGHT - 300, HEIGHT - 61)
        self.r = random.randint(10, 50)
        self.points = 0
        self.live = 1
        self.color = RED
        self.Vx = random.randint(-10, 10)
        self.Vy = random.randint(-10, 10)

    def move(self):
        self.x += self.Vx
        self.y += self.Vy
        if self.x >= WIDTH - self.r or self.x <= self.r:
            self.Vx = - self.Vx
        elif self.y >= HEIGHT - self.r or self.y <= self.r:
            self.Vy = - self.Vy

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(WIDTH - 200, WIDTH - 61)
        self.y = random.randint(HEIGHT - 300, HEIGHT - 61)
        self.r = random.randint(10, 50)
        self.live = 1
        self.Vx = random.randint(-10, 10)
        self.Vy = random.randint(-10, 10)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.r)

class Laser:
    def __init__(self):
        self.screen = screen
        self.angle = 0
        self.r = 0
        self.firing = 0
        self.color = GREY

    def fire_start(self):
        self.firing = 1

    def fire_end(self):
        self.firing = 0

    def draw(self):
        pygame.draw.line(self.screen, RED, (20, (HEIGHT / 2)), (20 + math.cos(gun.an) * 2*WIDTH, (HEIGHT / 2) + math.sin(gun.an) * 2*WIDTH), width=20)
        pygame.draw.line(self.screen, ORANGE, (20, (HEIGHT / 2)), (20 + math.cos(gun.an) * 2*WIDTH, (HEIGHT / 2) + math.sin(gun.an) * 2*WIDTH), width=8)
        pygame.draw.line(self.screen, YELLOW, (20, (HEIGHT / 2)), (20 + math.cos(gun.an) * 2*WIDTH, (HEIGHT / 2) + math.sin(gun.an) * 2*WIDTH), width=2)

    #def lensdraw(self):
    #        # y = 450, x = 20
    #    pygame.draw.line(self.screen, self.color, (20, (HEIGHT / 2)), (20 + math.cos(self.angle) * gun.f2_power, (HEIGHT / 2) + math.sin(self.angle) * gun.f2_power), width=10)

    def targetting(self, event):
        if event:
            self.angle = math.atan2((event.pos[1]-(HEIGHT/2)), (event.pos[0]-20))
        if self.firing:
            self.color = RED
        else:
            self.color = GREY

    def hittest_laser(self, obj):
        if abs(math.sin(self.angle)*obj.x - math.cos(self.angle)*obj.y - math.sin(self.angle)*20 + math.cos(self.angle)*(HEIGHT/2)) <= 10 + obj.r:
            return True
        else:
            return False

ammo = 0

def ammo_change(a:int):
    global ammo
    if a == 1:
        ammo = 0
    elif a == 0:
        ammo = 1
    print(a)

pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target()
target2 = Target()
laser = Laser()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()

    if ammo == 0:
        for b in balls:
            b.draw()
    elif laser.firing == 1:
        laser.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ammo == 0:
                gun.fire2_start(event)
            elif ammo == 1:
                laser.fire_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            if ammo == 0:
                gun.fire2_end(event)
            elif ammo == 1:
                laser.fire_end()
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            laser.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                ammo_change(ammo)

    target1.move()
    target2.move()

    if ammo == 0:
        for b in balls:
            b.move()
            if b.hittest(target1) and target1.live:
                target1.live = 0
                target1.hit()
                target1.new_target()
            if b.hittest(target2) and target2.live:
                target2.live = 0
                target2.hit()
                target2.new_target()

    if ammo == 1:
        if laser.hittest_laser(target1) and target1.live:
            target1.live = 0
            target1.hit()
            target1.new_target()
        if laser.hittest_laser(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2.new_target()
    gun.power_up()

pygame.quit()
pygame.font.quit()
pygame.mixer.quit()
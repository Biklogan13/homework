import math
from random import choice
import random
import pygame


FPS = 60

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = 0x7D7D7D
GAME_COLORS = [BLACK, RED, GREEN]

#WIDTH = 850*2
#HEIGHT = 500*2


class Ball:
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = gun.x
        self.y = gun.y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.live = 30
        self.angle = math.atan2(self.vy, self.vx)
        self.bullet = bullet

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        if self.y >= 2*HEIGHT - self.r:
            self.vy = 0
            self.vx = 0
        else:
            self.vy += 0.5
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        self.angle = math.atan2(self.vy, self.vx)
        #pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        self.bullet = rot_center(bullet, self.angle*360/(-2*math.pi))
        self.screen.blit(self.bullet, (self.x - 20, self.y - 20))

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
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.Vx = 0
        self.Vy = 0
        self.ax = 0
        self.ay = 0

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = 30 * math.cos(self.an)
        new_ball.vy = 30 * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.pos[1]-self.y), (event.pos[0]-self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        #y = 450, x = 20
        #pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x + math.cos(self.an)*self.f2_power, self.y + math.sin(self.an)*self.f2_power), width=10)
        #pygame.draw.circle(self.screen, GREY, (self.x, self.y), 20)
        self.screen.blit(ufo, (self.x - 55, self.y - 31))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 5
            self.color = RED
        else:
            self.color = GREY

    def move(self):

        if pygame.key.get_pressed()[pygame.K_w]:
            self.ay = -1
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.ay = 1
        else:
            self.ay = 0

        if pygame.key.get_pressed()[pygame.K_a]:
            self.ax = -1
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.ax = 1
        else:
            self.ax = 0

        if self.ax >= 0:
            if self.Vx <= 10:
                self.Vx += self.ax
        if self.ax <= 0:
            if self.Vx >= -10:
                self.Vx += self.ax
        if self.ay >= 0:
            if self.Vy <= 10:
                self.Vy += self.ay
        if self.ay <= 0:
            if self.Vy >= -10:
                self.Vy += self.ay

        if self.Vx >= 0:
            if self.x <= WIDTH:
                self.x += self.Vx
        if self.Vx <= 0:
            if self.x >= 0:
                self.x += self.Vx
        if self.Vy >= 0:
            if self.y <= HEIGHT:
                self.y += self.Vy
        if self.Vy <= 0:
            if self.y >= 0:
                self.y += self.Vy


class Target:
    def __init__(self):
        self.x = random.randint(71, WIDTH - 71)
        self.y = random.randint(71, 150)
        self.r = 35
        self.points = 0
        self.live = 1
        self.color = RED
        self.Vx = random.randint(-10, 10)
        self.Vy = random.randint(-10, 10)

    def move(self):
        self.x += self.Vx
        self.y += self.Vy
        if self.x >= WIDTH - self.r - 10 or self.x <= self.r + 10:
            self.Vx = - self.Vx
        elif self.y >= HEIGHT - self.r - 10 or self.y <= self.r + 10:
            self.Vy = - self.Vy

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(71, WIDTH - 71)
        self.y = random.randint(71, 150)
        self.r = 35
        self.live = 1
        self.Vx = random.randint(-10, 10)
        self.Vy = random.randint(-10, 10)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        #pygame.draw.circle(screen, RED, (self.x, self.y), self.r)
        screen.blit(mark, (self.x - 35, self.y - 45))

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
        pygame.draw.line(self.screen, RED, (gun.x, gun.y), (gun.x + math.cos(self.angle) * 2*WIDTH, gun.y + math.sin(self.angle) * 2*WIDTH), width=20)
        pygame.draw.line(self.screen, ORANGE, (gun.x, gun.y), (gun.x + math.cos(self.angle) * 2*WIDTH, gun.y + math.sin(self.angle) * 2*WIDTH), width=8)
        pygame.draw.line(self.screen, YELLOW, (gun.x, gun.y), (gun.x + math.cos(self.angle) * 2*WIDTH, gun.y + math.sin(self.angle) * 2*WIDTH), width=2)
        self.screen.blit(ufo, (gun.x - 55, gun.y - 31))

    #def lensdraw(self):
    #        # y = 450, x = 20
    #    pygame.draw.line(self.screen, self.color, (20, (HEIGHT / 2)), (20 + math.cos(self.angle) * gun.f2_power, (HEIGHT / 2) + math.sin(self.angle) * gun.f2_power), width=10)

    def targetting(self, event):
        if event:
            self.angle = math.atan2((event.pos[1]-gun.y), (event.pos[0]-gun.x))
        if self.firing:
            self.color = RED
        else:
            self.color = GREY

    def hittest_laser(self, obj):
        if abs(math.sin(self.angle)*obj.x - math.cos(self.angle)*obj.y - math.sin(self.angle)*gun.x + math.cos(self.angle)*gun.y) <= 10 + obj.r and (pygame.mouse.get_pos()[0] - gun.x)*(obj.x - gun.x) > 0 and self.firing == 1:
            return True
        else:
            return False


class Meta:
    def __init__(self):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.vy = 5
    def draw(self):
        self.screen.blit(bomb, (self.x - 60, self.y - 20))

    def move(self):
        if self.y >= 2*HEIGHT:
            self.vy = 0
        else:
            self.vy += 0.2
        self.y += self.vy

    def hittest(self):
        #if self.x <= gun.x + 55 + 25 and self.x > gun.x - 55 - 70 - 25 and self.y > gun.y - 31 - 75 and self.y < gun.y + 31 - 5:
        if (self.x - gun.x)**2 + (self.y - 20 - gun.y)**2 <= (35 + 45)**2:
            return True
        else:
            return False

ammo = 0

def ammo_change(a:int):
    global ammo
    if a == 1:
        ammo = 0
        laser.fire_end()
        pygame.mixer.Sound.stop(laser_sound)
    elif a == 0:
        ammo = 1
    print(a)

def hint():
    font1 = pygame.font.SysFont('arial', int(50 * HEIGHT / 1500))
    text1 = "Press SHIFT to change ammo"
    text2 = 'Press W,A,S,D to move'
    tekst = font1.render(text1, True, BLACK)
    screen.blit(tekst, (10, 10))
    tekst = font1.render(text2, True, BLACK)
    screen.blit(tekst, (10, 50))

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

pygame.init()
pygame.font.init()
pygame.mixer.init()
#screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.NOFRAME)
pygame.display.toggle_fullscreen()
balls = []
metas = []
#balloon = pygame.image.load('pngfind.com-captain-planet-png-6387166.png')
#balloon = pygame.transform.scale(balloon, (96, 163))

#blast = pygame.image.load('image.png')
#blast = pygame.transform.scale(blast, (400, 400))

background = pygame.image.load('How-ice-forms-inside-of-clouds-850x500.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

bullet = pygame.image.load('bullets-clip-art-129.png')
bullet = pygame.transform.scale(bullet, (40, 40))

ufo = pygame.image.load('pngegg.png')
ufo = pygame.transform.scale(ufo, (109, 62))

mark = pygame.image.load('Adobe_20211107_235838.png')
mark = pygame.transform.scale(mark, (70, 70))

bomb = pygame.image.load('Meta-Symbol.png')
bomb = pygame.transform.scale(bomb, (120, 80))

laser_sound = pygame.mixer.Sound('LaserLaserBeam EE136601_preview-[AudioTrimmer.com].mp3')
cannon_sound = pygame.mixer.Sound('ES_Cannon Blast 4.mp3')
ufo_explosion = pygame.mixer.Sound('soundscrate-bomb-explosion-1.mp3')
background_music = pygame.mixer.Sound('8-bit-skyway-1980s-style-music-122195828_prev.mp3')

pygame.mixer.Sound.set_volume(cannon_sound, 0.6)
pygame.mixer.Sound.set_volume(laser_sound, 0.6)
pygame.mixer.Sound.set_volume(background_music, 0.4)

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target()
target2 = Target()
laser = Laser()
finished = False
gun_movement = 0
pygame.mixer.Sound.play(background_music)
seconds = 1

while not finished:
    screen.blit(background, (0, 0))
    #screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()
    hint()
    #screen.blit(balloon, (500, 500))
    #screen.blit(blast, (350, 370))

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ammo == 0:
                gun.fire2_start(event)
            elif ammo == 1:
                laser.fire_start()
                pygame.mixer.Sound.play(laser_sound)
        elif event.type == pygame.MOUSEBUTTONUP:
            if ammo == 0:
                gun.fire2_end(event)
                pygame.mixer.Sound.play(cannon_sound)
            elif ammo == 1:
                laser.fire_end()
                pygame.mixer.Sound.stop(laser_sound)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            laser.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                ammo_change(ammo)
            if event.key == pygame.K_BACKSPACE:
                finished = True

    laser.angle = math.atan2((pygame.mouse.get_pos()[1] - gun.y), (pygame.mouse.get_pos()[0] - gun.x))

    gun.move()

    for b in balls:
        b.draw()

    if laser.firing == 1:
        laser.draw()

    target1.move()
    target2.move()

    for b in balls:
        b.move()

    for b in balls:
        if b.hittest(target1) and target1.live:
            target1.live = 0
            target1.hit()
            target1.new_target()
            pygame.mixer.Sound.play(ufo_explosion)
        if b.hittest(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2.new_target()
            pygame.mixer.Sound.play(ufo_explosion)

    if ammo == 1:
        if laser.hittest_laser(target1) and target1.live:
            target1.live = 0
            target1.hit()
            target1.new_target()
            pygame.mixer.Sound.play(ufo_explosion)
        if laser.hittest_laser(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2.new_target()
            pygame.mixer.Sound.play(ufo_explosion)

    if seconds % 60 == 0:
        new_bomb1 = Meta()
        new_bomb2 = Meta()
        new_bomb1.x = target1.x
        new_bomb1.y = target1.y
        new_bomb2.x = target2.x
        new_bomb2.y = target2.y
        #new_bomb1.vy += target1.Vy
        #new_bomb2.vy += target2.Vy
        metas.append(new_bomb1)
        metas.append(new_bomb2)

    for m in metas:
        m.draw()
        m.move()

    for m in metas:
        if m.hittest():
            finished = True

    gun.power_up()
    seconds += 1
    pygame.display.update()

pygame.mixer.Sound.stop(laser_sound)
pygame.mixer.Sound.stop(background_music)
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                finished = True

    screen.fill(BLACK)
    font1 = pygame.font.SysFont('arial', int(200 * HEIGHT / 1500))
    text1 = "GAME OVER"
    tekst1 = font1.render(text1, True, WHITE)
    screen.blit(tekst1, (WIDTH*0.25, HEIGHT*0.4))
    font2 = pygame.font.SysFont('arial', int(50 * HEIGHT / 1500))
    text2 = "PRESS BACKSPACE TO QUIT"
    tekst2 = font2.render(text2, True, WHITE)
    screen.blit(tekst2, (WIDTH*0.35, HEIGHT*0.6))
    pygame.display.update()

pygame.quit()
pygame.font.quit()
pygame.mixer.quit()
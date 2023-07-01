import pygame as pg
import random
pg.init()
win_width, win_height = 800, 600
window = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("Шутер")
class GameSprite:
    def __init__(self, image, x, y, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pg.transform.scale(pg.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def control1(self):
        keys = pg.key.get_pressed()
        if keys [pg.K_s] and self.rect.y < 600 - 100:
            self.rect.y += self.speed
        if keys [pg.K_w] and self.rect.y > 0 - 100:
            self.rect.y -= self.speed
    def control2(self):        
        keys = pg.key.get_pressed()
        if keys [pg.K_DOWN] and self.rect.y < 600 - 100:
            self.rect.y += self.speed
        if keys [pg.K_UP] and self.rect.y > 0 - 100:
            self.rect.y -= self.speed
class Boll(GameSprite):
    def move(self):
        global x2, y2, player1, player2
        self.rect.x += x2
        self.rect.y += y2
        if pg.sprite.collide_rect(player2, self):
            x2 = -4
        if pg.sprite.collide_rect(player1, self):
            x2 = 4
        if self.rect.y < 0:
            y2 = 4
        if self.rect.y > 550:
            y2 = -4
x2, y2 = 2, 2
back = GameSprite("image/fon.png", 0, 0, 800, 600, 0)
pwin1 = GameSprite("image/p1win.png", 0, 0, 800, 600, 0)
pwin2 = GameSprite("image/p2win.png", 0, 0, 800, 600, 0)
player1 = Player("image/1Player.png", 0, 300, 20, 150, 5)
player2 = Player("image/2Player.png", 780, 300, 20, 150, 5)
ball = Boll("image/boll.png", 450, 275, 75, 50, 5)
game = True
score1 = 0
score2 = 0
while game:
    pg.time.Clock().tick(144)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    if ball.rect.x < 0:
        score1 += 1
        ball.rect.x = 400
    if score1 >= 3:
        game_over = "image/p2win.png"
        game = False
    if ball.rect.x > 800:
        score2 += 1
        ball.rect.x = 400
    if score2 >= 3:
        game_over = "image/p1win.png"
        game = False
    back.reset()
    player1.reset()
    player1.control1()
    player2.reset()
    player2.control2()
    ball.reset()
    ball.move()
    label = pg.font.SysFont("Exo", 27).render(f"miss ball: {score1}", True, "red")
    window.blit(label,(20, 20))
    label2 = pg.font.SysFont("Exo", 27).render(f"miss ball: {score2}", True, "red")
    window.blit(label2,(675, 20))
    pg.display.flip()
bg = GameSprite(game_over, 0, 0, 800, 600, 0)
bg2 = GameSprite(game_over, 0, 0, 800, 600, 0)
while True:
    pg.time.Clock().tick(100)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    bg.reset()
    bg2.reset()
    pg.display.flip()
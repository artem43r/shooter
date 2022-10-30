#Создай собственный Шутер!
from random import randint
from pygame import *
font.init()
mixer.init()
mixer.music.load('space.mp3')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
count = 0
count2 = 0
f1 = font.SysFont('Arial', 36)
f2 = font.SysFont('Arial', 50)
text1 = f1.render('Счет:', True, (255, 255, 255))
text2 = f1.render('Пропущено:', True, (255, 255, 255))
text3 = f2.render('YOU WIN', True, (255, 215, 0))
text4 = f2.render('YOU LOSE', True, (200, 0, 0))




window = display.set_mode((700, 500))
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
sprite1 = 'rocket.png'
sprite2 = 'asteroid.jpg'
sprite3 = 'ufo.jpg'
sprite4 = 'bullet.jpg'

clock = time.Clock()
FPS = 60 
game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < 631:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(sprite4, self.rect.centerx - 30, self.rect.top, 7)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global count2
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(0, 700)
        if self.rect.y < 500:
            self.rect.y += self.speed
        if self.rect.y >= 500:
            count2 += 1
class Asteroid(GameSprite):
    def update(self):
        global count2
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(0, 700)
        if self.rect.y < 500:
            self.rect.y += self.speed
            self.rect.x += self.speed
        if self.rect.y >= 500:
            count2 += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y = self.rect.y - 10
        if self.rect.y <= 0:
            self.kill()

hero = Player(sprite1, 500, 400, 7)




monsters = sprite.Group()
bullets = sprite.Group()


for i in range(3):
    enemy = Enemy(sprite2, randint(0, 500), 0, 3)
    enemy2 = Asteroid(sprite3, randint(0, 500), 0, 4)
    monsters.add(enemy)
    monsters.add(enemy2)

while game == True:
    for i in event.get():
            if i.type == QUIT:
                game = False
            elif i.type == KEYDOWN:
                if i.key == K_SPACE:
                    fire_sound.play()
                    hero.fire()
    if not finish:
        clock.tick(FPS)
        window.blit(background, (0, 0))
        hero.update()
        hero.reset()
        enemy.update()
        enemy.reset()
        enemy2.update()
        enemy2.reset()
        bullets.draw(window)
        bullets.update()
        monsters.draw(window)
        monsters.update()
        text5 = f1.render(str(0), True, (255, 255, 255))
        text6 = f1.render(str(0), True, (255, 255, 255))
        collides = sprite.groupcollide(monsters, bullets, True, True)
        
        for i in collides:
            count += 1
            enemy = Enemy(sprite2, randint(0, 500), 0, 3)
            monsters.add(enemy)
        text5 = f1.render(str(count), True, (255, 255, 255))
        text6 = f1.render(str(count2), True, (255, 255, 255))

            
        window.blit(text1, (10, 50))
        window.blit(text2, (10, 80))
        if count > 10:
            window.blit(text3, (250, 80))
            finish = True
        if count2 > 3:
            window.blit(text4, (250, 80))
            finish = True
        window.blit(text5, (80, 50))
        window.blit(text6, (170, 80))
        display.update()
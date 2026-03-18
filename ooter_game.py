#создай игру "Лабиринт"!
from pygame import *
from random import randint
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.angle = 0
        self.delta_angle = choice([-10,-8,-6,-4,-2,2,4,6,8,10])
        self.origin_img = self.image
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -=  self.speed 
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x +=  self.speed  
    def iscollide(self,enemy):
        return sprite.collide_rect(self,enemy)
    def fire(self):
        pass

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 450:
            self.rect.x = randint(50, 600)
            self.rect.y = 10
            self.speed = randint(3,5)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
    


window = display.set_mode((700,500))
display.set_caption('шутер')
backgrounds = transform.scale(image.load('galaxy.jpg'), (700,500))
player = Player('GOIDA.png.png',330,350,100,100,10)
enemy = Enemy("ufo.png",player_x = randint(50,600),player_y = 10,size_x = 100,size_y = 50, player_speed = randint(5,8))


enemes = sprite.Group()
for i in range(5):
    enemy = Enemy("ufo.png",player_x = randint(50,600),player_y = 10,size_x = 100,size_y = 50, player_speed = randint(5,8))
    enemes.add(enemy)

enemes_killed = 0
counter_killed = font.SysFont('arial', 18, bold=True)
window.blit(surf_enemes_killed, (10, 15))
mixer,init()


mixer.init()
mixer.music.load('space.ogg')
#mixer.music.play()
kick = mixer.Sound('fire.ogg')

timer = time.Clock()

WHITE = (255,255,255)
lost = 0 
enemes_killed = 0

font.init()
f1 = font.Font(None, 70).render("YOU FOX",True,(103,0,200))
f2 = font.Font(None, 70).render("YOU LOX",True,(103,0,200))
counter_lost = font.SysFont('arial',18,bold=True)

timer = time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.tipe == KEYDOWN and e.key == K_SPACE:
            player.fire()
            fire_sound.play()
    if finish == False
    collides = sprite.groupcollide(enemes,bullets,True,True)
    for c in collides:
        enemes_killed += 1
        enemy = Enemy('ufo.png', randint(50, 650), 10, 90, 45, randint(1, 3))
        enemes.add(enemy)
    
    if lost > 5

    surf_lost = counter_lost.render(f'Пропущенные враги: {str(lost)}', True, WHITE)
    surf_lost = counter_killed.render(f"Сбитые хохлы: {str(lost)}", True,)


    window.blit(backgrounds,(0,0))
    window.blit(surf_lost,(10,30))
    player.reset()
    player.update()
    enemes.update()
    enemes.draw(window)
    display.update()
    timer.tick(60)
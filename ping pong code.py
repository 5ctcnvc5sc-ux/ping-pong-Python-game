from pygame import *
from random import randint
import time as tm
init()
mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, filename, width, height, x, y, step = 5):
        super().__init__()
        self.image = image.load(filename)
        self.rect = Rect(x, y, width, height)
        self.image = transform.scale(self.image, (width, height))
        self.x = x
        self.y = y
        self.step = step
        self.start_x = x
        self.start_y = y

    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y
        window.blit(self.image, (self.x, self.y))

class Rocket(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.x < window_size[0] - self.rect.width: self.x += self.step 
        if keys[K_a] and self.x > 0: self.x -= self.step 

#class Ball: 


class Label:
    def __init__(self, text, color, x, y, size):
        self.font = font.SysFont('verdana', size)
        self.label = self.font.render(text, True, color)
        self.text = text
        self.color = color
        self.coords = (x, y)

    def draw(self):
        window.blit(self.label, self.coords)

    def set_number(self, number):
        self.label = self.font.render(f'{self.text}: {number}', True, self.color)

#play background music
mixer.music.load('space.ogg')
mixer.music.set_volume(0.15)
mixer.music.play()

#add new background music for win / lose


metal_hit = mixer.Sound('metal_hit.mp3')
laser_gunshot = mixer.Sound('laser_gunshot.mp3')
stone_thud = mixer.Sound('stone_thud.mp3')

########
icon = image.load('.png')
icon = transform.scale(icon, (32, 32))
display.set_icon(icon)
########

window = display.set_mode((700, 500))
clock = time.Clock() #timer
window_size = window.get_size()

background = image.load('galaxy.jpg') 
background = transform.scale(background, window_size)

rocket = Player('rocket.png', 70, 70, 350, 400)


game_on = True
game_result = False
while game_on:
    for game_event in event.get():
        #k_q meaning the key q on your keyboard
        if game_event.type == QUIT:
            game_on = False
        if game_event.type == KEYDOWN:
            if game_event.key == K_ESCAPE:
                game_on = False

    if not game_result:

            
        rocket.update()


    window.fill((0, 0, 255))
    window.blit(background, (0, 0))
            
    rocket.draw()

    display.update()
    clock.tick(60) #fps frames per second

import pygame
from pygame.sprite import Sprite
from random import randint

def load_image(name):
    image = pygame.image.load(name)
    return image

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.images = []
        self.images.append(load_image('images/alien_1_frame0.png'))
        self.images.append(load_image('images/alien_1_frame1.png'))
        self.images.append(load_image('images/alien_1_frame2.png'))
        self.images.append(load_image('images/alien_1_frame3.png'))
        self.index = 0
        self.timer = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_settings. alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        if self.timer < 100:
            self.timer += 1
        else:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            self.timer = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)
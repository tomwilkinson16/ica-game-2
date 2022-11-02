import pygame
from pygame.locals import * #helps with image importing
from pygame import mixer

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
MAX_SPRITE_WIDTH = 40
MAX_SPRITE_HEIGHT = 40
BLACK = (0,0,0)

#load iamges
background = pygame.image.load('img/stars.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
start_img = pygame.image.load('img/start.png')
rules_img = pygame.image.load('img/rules.png')
restart_img = pygame.image.load('img/restart.png')
quit_img = pygame.image.load('img/quit.png')
resume_img = pygame.image.load('img/resume.png')
back_img = pygame.image.load('img/back.png')
dead_image = pygame.image.load('img/ghost.png')
dead_image = pygame.transform.scale(dead_image,(MAX_SPRITE_WIDTH, MAX_SPRITE_HEIGHT))
dead_image.set_colorkey(BLACK)


pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init() #starts pygame


#load sounds
pygame.mixer.music.load('img/music.wav')
pygame.mixer.music.play (-1, 0.0, 0)
shoot_fx = pygame.mixer.Sound ('img/laser.wav')
shoot_fx.set_volume(0.2)
gameover_fx = pygame.mixer.Sound ('img/gameover.wav')
gameover_fx.set_volume(0.5)
aliendead_fx = pygame.mixer.Sound ('img/aliendeath.wav')
aliendead_fx.set_volume(0.1)
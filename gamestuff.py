import pygame
import time
import sys
import random
from pygame.locals import *



FPS = 60
CLOCK = pygame.time.Clock()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dream Come True?") #Game name at top


#colours and fonts
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)
font = pygame.font.SysFont("monospace", 22)
fontbig = pygame.font.SysFont("monospace", 50)


'''fps updater in the top left of screen'''
def update_fps():
    fps = str(int(CLOCK.get_fps()))
    return fps


'''defines the grid of the window. 50 is the blocksize (That makes it 20 X 12)'''
def drawGrid():
    tile_size = 50 #Set the size of the grid tile
    for x in range(0, SCREEN_WIDTH, tile_size):
        for y in range(0, SCREEN_HEIGHT, tile_size):
            rect = pygame.Rect(x, y, tile_size, tile_size)
            pygame.draw.rect(WINDOW, WHITE, rect, 2)

'''draws text onto a screen using the draw method in the game loop. see (1) at the bottom of the screen'''
def draw_text(text, font, text_colour, x, y):
    img = font.render(text, True, text_colour)
    WINDOW.blit(img, (x, y))


'''This class helps to make buttons in game'''
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        
    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        #left click
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        #draw button
        WINDOW.blit(self.image, self.rect)
        pygame.draw.rect(WINDOW, (WHITE), self.rect, 2)

        return action

import pygame
import random

pygame.init()

# import all images
background = pygame.image.load('immagini/sfondo.png')
bird = pygame.image.load('immagini/uccello.png')
ground = pygame.image.load('immagini/base.png')
gameover = pygame.image.load('immagini/gameover.png')
pipe_down = pygame.image.load('immagini/tubo.png')
pipe_up = pygame.transform.flip(pipe_down, False, True)


#make the window game

screen = pygame.display.set_mode((288,512))
FPS = 50

def draw():
    screen.blit(background, (0,0))
    screen.blit(bird, (birdx,birdy))
    
def displayUpdate():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def start():
    global birdx, birdy, bird_vely
    birdx, birdy = 60, 150
    bird_vely = 0
    
start()

while True:
    bird_vely += 1
    birdy += bird_vely
    
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.type == pygame.K_UP):
            bird_vely = -10
        if(event.type == pygame.QUIT):
            pygame.quit()
    
    draw()
    displayUpdate()
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
velocity = 3

class pipe():
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75, 150)
    def go_and_draw(self):
        self.x -= velocity
        screen.blit(pipe_up, (self.x, self.y-210))
        screen.blit(pipe_down, (self.x, self.y+210))
    def collision(self, bird, birdx,birdy):
        range = 5
        bird_right = birdx + bird.get_width() - range
        bird_left = birdx + range
        pipe_right = self.x + pipe_down.get_width()
        pipe_left = self.x
        bird_top = birdy + range
        bird_bottom = birdy + bird.get_height() - range
        pipe_side_up = self.y + 110
        pipe_side_down = self.y + 210
        if bird_right > pipe_left and bird_left < pipe_right:
            if bird_top < pipe_side_up or bird_bottom > pipe_side_down:
                game_over()

def draw():
    screen.blit(background, (0,0))
    for p in pipes:
        p.go_and_draw()
    screen.blit(bird, (birdx,birdy))
    screen.blit(ground, (groundx,400))

    
def displayUpdate():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def start():
    global birdx, birdy, bird_vely
    global groundx
    global pipes
    groundx = 0
    birdx, birdy = 60, 150
    bird_vely = 0
    pipes = []
    pipes.append(pipe())


def game_over():
    screen.blit(gameover, (60,150))
    displayUpdate()
    restart = False
    while not restart:
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                start()
                restart = True
            if(event.type == pygame.QUIT):
                pygame.quit()


start()

while True:
    
    # ground 
    groundx -= velocity
    if groundx < -45: groundx = 0
    
    bird_vely += 1
    birdy += bird_vely
    
    # bird position
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            bird_vely = -10
        if(event.type == pygame.QUIT):
            pygame.quit()
            
    #pipe creation
    if pipes[-1].x < 100: pipes.append(pipe())
    for p in pipes:
        p.collision(bird, birdx, birdy)

    if birdy > 390:
        game_over()
                
    
    draw()
    displayUpdate()
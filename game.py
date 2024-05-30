import pygame
clock=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((600, 412))
icon=pygame.image.load("images/icon.png")
bg=pygame.image.load("images/background.jpg")
pygame.display.set_icon(icon)
pygame.display.set_caption("EstFinX's game")
x=0
while True:
    screen.blit(bg,(x+600,0))
    screen.blit(bg,(x,0))
    x-=1
    if x==-600:
        x=0
    pygame.display.update()
    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
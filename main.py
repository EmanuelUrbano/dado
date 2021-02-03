import pygame
import random

largura = 600
altura = 400
screen = pygame.display.set_mode((altura, largura))

listaDado =["d1.png","d2.png","d3.png","d4.png","d5.png","d6.png"]
botão = pygame.image.load("botao.png")
dado = pygame.image.load("d1.png")
loop = True
click = False
clock = pygame.time.Clock()

while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            dado = pygame.image.load(listaDado[random.randint(0,5)])

        

    screen.blit(dado, (30, 30))
    screen.blit(botão, (30, 500))
    clock.tick(1000)
    pygame.display.update()

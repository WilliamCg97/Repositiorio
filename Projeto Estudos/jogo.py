import pygame
from pygame.locals import *
from sys import exit 


pygame.init()


altura = 480 
largura = 640 

## defidino posição e tamanho da snake 
pos_x = largura / 2
pos_y = altura / 2

largura_snake= 30
altura_snake = 50



# Criando a janela 
tela = pygame.display.set_mode((largura, altura))

# Definindo titulo da janela 
pygame.display.set_caption ("Snake")

while True : 
    #Colocando eventos nno jogo , event.type == quit  para fecha o jogo 
    for event in pygame.event.get() : 
        if event.type == QUIT : 
            pygame.quit()
            exit()
    pygame.draw.rect(tela,(0,0,255),( pos_x , pos_y , largura_snake , altura_snake))
    
    pygame.draw.circle(tela(255,0,0),(10,20), 10)
    # Att o jogo a cada interação 
    pygame.display.update
    
    
    
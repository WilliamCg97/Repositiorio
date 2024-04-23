import pygame
from pygame.locals import *
from sys import exit 
from random import* 

pygame.init()


altura = 480 
largura = 640 

## defidino posição e tamanho da snake 
pos_x_snake = largura / 2
pos_y_snake = altura / 2

largura_snake= 30
altura_snake = 50
# posição circulo 
pos_y_circulo = 40
pos_x_circulo= 40
raio_circulo = 10


# Definindo fonte 
fonte = pygame.font.SysFont("arial" , 20 , True , False)
pontos= 0 

# Criando a janela 
tela = pygame.display.set_mode((largura, altura))

# Definindo titulo da janela 
pygame.display.set_caption ("Snake")

#modificando tava de att de pixel por segundo ; 

relogio = pygame.time.Clock()


while True : 
    relogio.tick(30)
    tela.fill((0,0,0))
    msg = f' pontos : {pontos}'
    texto_formatado = fonte.render(msg , True , (255 , 255 ,255 ))
    
    #Colocando eventos nno jogo , event.type == quit  para fecha o jogo 
    for event in pygame.event.get() : 
        if event.type == QUIT : 
            pygame.quit()
            exit()
        
        # definindo o evento da tecla sendo apertanda " keydown" , especificando a tecla up 
        # if event.type == KEYDOWN :
        #     if event.key == K_UP :  
        #         pos_y_snake -= 10   
                
        #     if event.key == K_DOWN : 
        #         pos_y_snake += 10
                
        #     if event.key == K_LEFT : 
        #         pos_x_snake -= 10     
        
        #     if event.key == K_RIGHT : 
        #         pos_x_snake += 10 
        
    if pygame.key.get_pressed()[K_UP] :
        pos_y_snake -= 10
    elif pygame.key.get_pressed() [K_LEFT] :
        pos_x_snake -= 10

    elif pygame.key.get_pressed() [K_RIGHT] :
        pos_x_snake += 10
            
    elif pygame.key.get_pressed() [K_DOWN] :
        pos_y_snake += 10
            
    snake = pygame.draw.rect(tela,(255,255,255),( pos_x_snake , pos_y_snake , largura_snake , altura_snake))
    tela.blit(texto_formatado , (400 , 40 ))
    
    
    # Definindo tamanho e posição do circulo
    circulo = pygame.draw.circle(tela,(255,0,0),(pos_x_circulo,pos_y_circulo), raio_circulo)
    # Att o jogo a cada interação 
    pygame.display.update()
    
    
    if snake.colliderect(circulo) : 
        pos_x_circulo = randint (40,600)
        
        pos_y_circulo = randint (40, 430)
        pontos +=1
        
        
        
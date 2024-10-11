#Example file showing a basic pygame "game loop"
import pygame #importa a bibliotecagit 

# pygame setup
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('jogo da Velha Wagner')
clock = pygame.time.Clock()

fonte_quadrinhos = pygame.font.SysFont( 'Comic Sans Ms' , 100) #importar fonte
running = True # variavel de controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('0', True, 'red')
cor_fundo = 1


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            cor_fundo = cor_fundo + 1
        if (cor_fundo > 3): 
            cor_fundo = 1
           
       
    if cor_fundo == 1:
        screen.fill('blue')
        screen.blit(personagem_x,(250,250))
    elif cor_fundo == 2:
        screen.blit(personagem_y,(250,250))
        screen.fill('blue')
    else:
        screen.fill('purple')
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    

pygame.quit()
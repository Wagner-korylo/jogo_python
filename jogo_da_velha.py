#Example file showing a basic pygame "game loop"
import pygame #importa a bibliotecagit 

# pygame setup
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600))#Essa função configura a janela onde o jogo será exibido
pygame.display.set_caption('jogo da Velha Wagner')# Essa função altera o titulo da janela que sera exibido no aplicativo
clock = pygame.time.Clock() #Essa função é usado para gerenciar a velocidade da atualização da tela
 
fonte_quadrinhos = pygame.font.SysFont ( 'Comic Sans Ms',100) #importar fonte
running = True #(a variavel running é usado como condição para determinar se o lup principal dp jogo deve continuar girando ou nao.quando
               #running e true o loop continua; quando o ruinng se torna falso

#redefinir os caracteres 'X' e '0'
personagem_x = fonte_quadrinhos.render ('X', True, 'red')#cria uma superficie de imagem apartir do texto que vc dseseja exibir da tela. X e 0
personagem_0 = fonte_quadrinhos.render ('0', True, 'red')

jogador_atual = personagem_x #inicializa o jogo vom o x

rodadas = 0  # essa vareavel é usada para um controle de cor de fundo da tela de um jogo, permitindo alternancia entre diferentes nucleos

coordenada_x = 0
coordenada_y = 0



while running:#usado para repetir um bloco do codigo quando uma condição é verdadeira
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():#essa função retorna uma lista de  todos os eventos que ocorree desde a ultima vez que voce chamou essa funçaõ
                                 #isso inclui envento com o clic de mouse teclas precionadas movimento de mouse e comando de fechamentos de janelas 
        if event.type == pygame.QUIT:# detecta quando um usuário tenta fexsr uma janela do jogo permite que vc respoonde a esse evento enserrando o 
                                 #loopng principal e fechando o jogo principal
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:# é uma seleção condicional que detecta, quando um botão do mouse for precionado.
            print('Clicou')#é um comando que exibe uma mensagem clicou no consoilo ou na saida padrao do programa.
            click_pos = pygame.mouse.get_pos() # a posição do mouse quando ouver evento do cli
            print('eixo x:' , click_pos[0])
            print('eixo y:' , click_pos [1])
            coordenada_x = click_pos[0]
            coordenada_y = click_pos[1]
            rodadas = rodadas + 1
            if rodadas >= 10:
                screen.fill('black')
                rodadas = 0
                coordenada_x = 0
                coordenada_y = 0


            if rodadas != 1:

                if jogador_atual == personagem_x :
                   jogador_atual = personagem_0  
                else:
                   jogador_atual = personagem_x   
            else:
                jogador_atual = personagem_x      

            #desenha tabuleiro 
    pygame.draw.line(screen, 'white',(200, 0),(200, 600),10)
    pygame.draw.line(screen, 'white',(400, 0),(400, 600),10)
    pygame.draw.line(screen, 'white',(0, 200),(600, 200),10)
    pygame.draw.line(screen, 'white',(0, 400),(600, 400),10)
           
     #primeira linha    
     #            x   y
    if  coordenada_x > 0 and coordenada_x < 200 and coordenada_y < 200:
        screen.blit(jogador_atual,(60,30))#  primeiro           preenche com o azul
    elif  coordenada_x >= 200 and coordenada_x < 400 and coordenada_y < 200:
        screen.blit(jogador_atual,(260,30))# segundo           para desenhar na superficie uma imagem ou um texto na tela com o x
    elif  coordenada_x >= 400 and coordenada_y <= 200:
        screen.blit(jogador_atual,(460,30))# terceiro          preenche com o azul

         #segunda  linha            x  y
    elif coordenada_x < 200 and coordenada_y >= 200 and coordenada_y < 400:
        screen.blit(jogador_atual,(60,230))# quarto             preenche com o azul
    elif coordenada_x >= 200 and coordenada_x < 400 and coordenada_y > 200 and coordenada_y < 400:
        screen.blit(jogador_atual, (260,230))#quinto             para desenhar na superficie uma imagem ou um texto na tela com o x
    elif coordenada_x >= 400 and coordenada_y >= 200 and coordenada_y< 400:
        screen.blit(jogador_atual, (460,230))# sexto             preenche com o azul

         #terceiralinha             x   y
    elif coordenada_x < 200 and coordenada_y >= 400:
        screen.blit(jogador_atual, (60,430))# setimo             preenche com o azul
    elif coordenada_x >= 200 and coordenada_x < 400 and coordenada_y >= 400:
        screen.blit(jogador_atual, (260,430))# oitavo             para desenhar na superficie uma imagem ou um texto na tela com o x
    elif coordenada_x >= 400 and coordenada_y >= 400:
        screen.blit(jogador_atual, (460,430))# nono               preenche com o azul

   
      
     # flip() the display to put your work on screen
    pygame.display.flip() # a area atualizar a tela do jogo com todas as alterações que foram feitas desde a ultima atualização

    clock.tick(60)  # limits FPS to 60, é um objeto utilizado para controlar opm tempo e a taxa atualização do jogo
    

pygame.quit()# enserrar a biblioteca e limpar todos os recursos que foram ultilizados diran te a execulção do jogo.
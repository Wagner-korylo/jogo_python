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
personagem_y = fonte_quadrinhos.render ('0', True, 'red')
apresenta_personagem = 0  # essa vareavel é usada para um controle de cor de fundo da tela de um jogo, permitindo alternancia entre diferentes nucleos
x = 0
y = 0



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
            click_pos = pygame.mouse.get_pos()
            print('eixo x:' , click_pos[0])
            print('eixo y:' , click_pos [1])
            x = click_pos[0]
            y = click_pos[1]
            apresenta_personagem = apresenta_personagem + 1
            if(apresenta_personagem >= 9): # é uma condiçaõ que verifica se o valar da veriavel cor fundo é >3 
                screen.fill('black')         
                apresenta_personagem = 0
               

            #desenha tabuleiro 
    pygame.draw.line(screen, 'white',(200, 0),(200, 600),10)
    pygame.draw.line(screen, 'white',(400, 0),(400, 600),10)
    pygame.draw.line(screen, 'white',(0, 200),(600, 200),10)
    pygame.draw.line(screen, 'white',(0, 400),(600, 400),10)
           
     #primeira linha    
     #            x   y
    if    x > 0 and x < 200 and y < 200:
         screen.blit(personagem_x,(60,30))#  primeiro           preenche com o azul
    elif x >= 200 and x < 400 and y < 200:
        screen.blit(personagem_y,(260,30))# segundo           para desenhar na superficie uma imagem ou um texto na tela com o x
    elif x >= 400 and y <= 200:
        screen.blit(personagem_y,(460,30))# terceiro          preenche com o azul

         #segunda  linha            x  y
    elif x < 200 and y > 200 and y <= 400:
        screen.blit(personagem_x,(60,230))# quarto             preenche com o azul
    elif x >= 200 and x< 400 and y> 200 and y >= 400:
        screen.blit(personagem_y, (260,230))#quinto             para desenhar na superficie uma imagem ou um texto na tela com o x
    elif x >= 400 and y >= 200 and Y < 400:
        screen.blit(personagem_y, (460,230))# sexto             preenche com o azul

         #terceiralinha             x   y
    elif x < 200 and y >= 400:
        screen.blit(personagem_x, (60,430))# setimo             preenche com o azul
    elif x >= 200 and x < 400 and Y >= 400:
        screen.blit(personagem_y, (260,430))# oitavo             para desenhar na superficie uma imagem ou um texto na tela com o x
    elif x >= 400 and y >= 400:
        screen.blit(personagem_y, (460,430))# nono               preenche com o azul

      
     # flip() the display to put your work on screen
    pygame.display.flip() # a area atualizar a tela do jogo com todas as alterações que foram feitas desde a ultima atualização

    clock.tick(60)  # limits FPS to 60, é um objeto utilizado para controlar opm tempo e a taxa atualização do jogo
    

pygame.quit()# enserrar a biblioteca e limpar todos os recursos que foram ultilizados diran te a execulção do jogo.
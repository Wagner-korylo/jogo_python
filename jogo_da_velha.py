#Example file showing a basic pygame "game loop"
import pygame #importa a bibliotecagit 

# pygame setup
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((500, 500))#Essa função configura a janela onde o jogo será exibido
pygame.display.set_caption('jogo da Velha Wagner')# Essa função altera o titulo da janela que sera exibido no aplicativo
clock = pygame.time.Clock() #Essa função é usado para gerenciar a velocidade da atualização da tela
 
fonte_quadrinhos = pygame.font.SysFont ( 'Comic Sans Ms',100) #importar fonte
running = True #(a variavel running é usado como condição para determinar se o lup principal dp jogo deve continuar girando ou nao.quando
               #running e true o loop continua; quando o ruinng se torna falso

#redefinir os caracteres 'X' e '0'
personagem_x = fonte_quadrinhos.render ('X', True, 'red')#cria uma superficie de imagem apartir do texto que vc dseseja exibir da tela. X e 0
personagem_y = fonte_quadrinhos.render ('0', True, 'red')
cor_fundo = 1# essa vareavel é usada para um controle de cor de fundo da tela de um jogo, permitindo alternancia entre diferentes nucleos



while running:#usado para repetir um bloco do codigo quando uma condição é verdadeira
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():#essa função retorna uma lista de  todos os eventos que ocorree desde a ultima vez que voce chamou essa funçaõ
                                 #isso inclui envento com o clic de mouse teclas precionadas movimento de mouse e comando de fechamentos de janelas 
        if event.type == pygame.QUIT:# detecta quando um usuário tenta fexsr uma janela do jogo permite que vc respoonde a esse evento enserrando o 
                                 #loopng principal e fechando o jogo principal
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:# é uma seleção condicional que detecta, quando um botão do mouse for precionado.
            print ('Clicou')#é um comando que exibe uma mensagem clicou no consoilo ou na saida padrao do programa.
            cor_fundo += 1# 
        if (cor_fundo > 3): # é uma condiçaõ que verifica se o valar da veriavel cor fundo é >3           
            cor_fundo = 1#
           
       
    if cor_fundo == 1:# condicional que execulta um codigo de bloco se a condição especificada for verdadeira neste caso ela verifica se cor fundo é ugual a 1.2
         screen.fill('blue')# preencha toda a estrutura do jogo com a cor específica azul
         screen.blit(personagem_x, (250,250))#para desenhar na superficie uma imagem ou um texto na tela com o x
    elif cor_fundo == 2:#verifique se a cor de fundo será a 2, para deternimar que açaõ a ser tomada, 
         screen.fill('blue')# preenche com o azul
         screen.blit(personagem_y, (250,250))#para desenhar na superficie uma imagem ou um texto na tela com o y
         
    else:
         screen.fill('purple') #preenche com a cor roxa
    

    # flip() the display to put your work on screen
    pygame.display.flip() # a area atualizar a tela do jogo com todas as alterações que foram feitas desde a ultima atualização

    clock.tick(60)  # limits FPS to 60, é um objeto utilizado para controlar opm tempo e a taxa atualização do jogo
    

pygame.quit()# enserrar a biblioteca e limpar todos os recursos que foram ultilizados diran te a execulção do jogo.
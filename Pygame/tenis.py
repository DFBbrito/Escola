import pygame

pygame.init()

#Janela do jogo
width=800
height=600
title="Tenis"
window=pygame.display.set_mode((width,height))
pygame.display.set_caption(title)

clock=pygame.time.Clock()

VELOCIDADE_GERAL=2
FUNDO=0,0,75

#jogador
ficheiro_player="imagens/raquete1.png"
speedx_player=0
speedy_player=1
imagem_player=pygame.image.load(ficheiro_player)
rect_player=imagem_player.get_rect()
rect_player.topleft=(40,300)

#cpu
ficheiro_cpu="imagens/raquete2.png"
speedx_cpu=0
speedy_cpu=VELOCIDADE_GERAL
imagem_cpu=pygame.image. load(ficheiro_cpu)
rect_cpu=imagem_cpu.get_rect()
rect_cpu.topleft=(740,300)

#bola
ficheiro_bola="imagens/bola.png"
speedx_bola=VELOCIDADE_GERAL
speedy_bola=VELOCIDADE_GERAL
imagem_bola=pygame.image.load(ficheiro_bola)
rect_bola=imagem_bola.get_rect()
rect_bola.topleft=(400,300)

run=True
while run:
    #Logica do jogo
    #Player
    rect_player=rect_player.move(speedx_player,speedy_player)
    #bola
    rect_bola=rect_bola.move(speedx_bola,speedy_bola)
    #detetar colisoes
    #bola no fundo e topo do ecrã
    if rect_bola.top<=0 or rect_bola.top+rect_bola.height>height:
        speedy_bola=speedy_bola*-1
    if rect_bola.colliderect(rect_player) or rect_bola.colliderect(rect_cpu):
        speedx_bola=speedx_bola*-1

    #movimento cpu
    if rect_bola.top<rect_cpu.top:
        speedy_cpu=-VELOCIDADE_GERAL
    if rect_bola.top>rect_cpu.top:
        speedy_cpu=VELOCIDADE_GERAL
    rect_cpu=rect_cpu.move(speedx_cpu,speedy_cpu)

    #desenhar
    window.fill(FUNDO)

    #jogador
    window.blit(imagem_player,rect_player)
    #cpu
    window.blit(imagem_cpu,rect_cpu)
    #bola
    window.blit(imagem_bola,rect_bola)
    
    #atualiza
    pygame.display.flip()
    clock.tick(60)
    #ler os inputs 
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                speedy_player=-VELOCIDADE_GERAL
            if event.key==pygame.K_DOWN:
                speedy_player=VELOCIDADE_GERAL
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                run=False
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False

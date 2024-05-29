import pygame
import sys
import random

# Definição de constantes
WIDTH, HEIGHT = 800, 600
TITLE = "Tenis"
VELOCIDADE_BOLA = 6              # Velocidade da bola
FUNDO = (0, 0, 75)

# Definição de cores
BRANCO = (255, 255, 255)

# Classe para representar a raquete controlada pela IA
class IA(pygame.sprite.Sprite):
    def __init__(self, imagem, posicao, velocidade):
        super().__init__()
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect(topleft=posicao)
        self.velocidade = velocidade
        self.pontuacao = 0

    def move(self, ball):
        # Movimento da raquete baseado na posição da bola
        if self.rect.centery < ball.rect.centery:
            self.rect.y += self.velocidade
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
        elif self.rect.centery > ball.rect.centery:
            self.rect.y -= self.velocidade
            if self.rect.top < 0:
                self.rect.top = 0

    def update(self, ball):
        self.move(ball)

# Classe para representar a bola
class Bola(pygame.sprite.Sprite):
    def __init__(self, imagem, posicao):
        super().__init__()
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect(center=posicao)
        self.speedx = VELOCIDADE_BOLA
        self.speedy = VELOCIDADE_BOLA

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speedy *= -1

# Função principal do jogo
def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # Criar objetos do jogo
    ia_player = IA("imagens/raquete1.png", (40, 300), 6)
    ia_cpu = IA("imagens/raquete2.png", (740, 300), 6)
    bola = Bola("imagens/bola.png", (400, 300))

    # Loop principal do jogo
    run = True
    while run:
        # Eventos do pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        # Atualizar objetos do jogo
        bola.update()
        ia_player.update(bola)
        ia_cpu.update(bola)

        # Detectar colisão entre a bola e as raquetes
        if bola.rect.colliderect(ia_player.rect) or bola.rect.colliderect(ia_cpu.rect):
            bola.speedx *= -1

        # Atualizar a tela
        window.fill(FUNDO)
        window.blit(ia_player.image, ia_player.rect)
        window.blit(ia_cpu.image, ia_cpu.rect)
        window.blit(bola.image, bola.rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

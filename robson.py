import pygame
import random

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Balacobaco!")

# Cores
cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (138, 43, 226), (0, 255, 255)]

# Define a posição inicial do círculo
x = random.randint(50, largura_tela - 50)
y = random.randint(50, altura_tela - 50)
raio = 50
velocidade_x = 5
velocidade_y = 5

# Controla a execução do jogo
executando = True
clock = pygame.time.Clock()

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Preenche a tela com uma cor de fundo
    tela.fill((0, 0, 0))

    # Altera a cor do círculo aleatoriamente
    cor_circulo = random.choice(cores)

    # Atualiza a posição do círculo
    x += velocidade_x
    y += velocidade_y

    # Se o círculo colidir com as bordas da tela, inverte a direção
    if x + raio > largura_tela or x - raio < 0:
        velocidade_x = -velocidade_x
    if y + raio > altura_tela or y - raio < 0:
        velocidade_y = -velocidade_y

    # Desenha o círculo na tela
    pygame.draw.circle(tela, cor_circulo, (x, y), raio)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros
    clock.tick(60)

# Finaliza o Pygame
pygame.quit()

import pygame
pygame.init()
janela = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Primeiro jogo')
#larguradetela = 500
y = 50
x = 50
largura = 40
altura = 60
velocidade = 5
pular = False
contapulo = 10
correr = True
while correr:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]or keys[pygame.K_a]and x > velocidade:
        x -= velocidade
      #x = x - velocidade é a mesma coisa disso.
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and x < 1000 - largura - velocidade:
        x += velocidade
      #x = x + velocidade é a mesma coisa disso.
    if not (pular):
        if keys[pygame.K_UP] or keys[pygame.K_w] and y > velocidade:
            y -= velocidade
          #y = y - velocidade é a mesma coisa disso.
        if keys[pygame.K_DOWN] or keys[pygame.K_s] and y < 500 - altura - velocidade:
            y += velocidade
          #y = y - velocidade é a mema coisa disso.
        if keys[pygame.K_SPACE]:
            pular = True
    else:
        if contapulo >= -10:
            negativo = 1
            if contapulo < 0:
                negativo = -1
            y -= (contapulo ** 2) * 0.5 * negativo
                                 #OU  /2
            contapulo -= 1
        else:
            pular = False
            contapulo = 10
    janela.fill((0, 0, 0))
    pygame.draw.rect(janela, (255, 0, 0), (x, y, largura, altura))
    pygame.display.update()

pygame.quit()


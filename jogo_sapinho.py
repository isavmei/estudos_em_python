import pygame
import random 
import sys

pygame.init()

largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("sapinho")

branco = (255, 255, 255)
verde = (0, 200, 0)
vermelho = (200, 0, 0)
preto = (0, 0, 0)

fonte = pygame.font.SysFont(None, 48)

posicao_mosca = random.randint(1,5)

pedrinhas = []
for i in range(5):
    pedrinhas.append(pygame.Rect(60 + i * 100, 150, 80, 80))

mensagem = ""
rodando = True
while rodando: 
 tela.fill(branco)
 for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i, pedra in enumerate(pedrinhas):
                if pedra.collidepoint(evento.pos):
                    if i + 1 == posicao_mosca:
                        mensagem = "BROGUET!"
                    else:
                        mensagem = "fome!"

    
        for i, pedra in enumerate(pedrinhas):
            pygame.draw.rect(tela, verde, pedra)
            num_text = fonte.render(str(i+1), True, preto)
            tela.blit(num_text, (pedra.x + 25, pedra.y + 20))

    
        if mensagem:
            texto = fonte.render(mensagem, True, vermelho if mensagem == "fome!" else preto)
            tela.blit(texto, (200, 50))

        pygame.display.flip()

pygame.quit()
sys.exit()
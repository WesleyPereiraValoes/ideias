import pygame 
from random import randint

pygame.init()

WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)

cor = [0,0]

local = [40,40]

clock = pygame.time.Clock()
# cria a janela
size = (100, 100)
screen = pygame.display.set_mode(size)
# escreve no titulo
pygame.display.set_caption("Teste")

# define o keyboard
def keydown(valor):
	if valor.key == 273:
		cor[1] = cor[1] - 1
	elif valor.key == 274:
		cor[1] = cor[1] + 1
	elif valor.key == 276:
		cor[0] = cor[0] - 1
	elif valor.key == 275:
		cor[0] = cor[0] + 1

# define o jogador a cpu e a colisao
def game():
	jogador = pygame.draw.rect(screen, BLACK, [cor[0],cor[1],10,10])
	
	human = pygame.draw.rect(screen, GREEN, [local[0],local[1],10,10])

	if jogador[0] == human[0] or jogador[1] == human[1]:
		local[0] = randint(0,50)
		local[1] = randint(0,50)

# loop para renderizar a tela
done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYUP:
			pass
		elif event.type == pygame.KEYDOWN:
			keydown(event)

	screen.fill((WHITE))

	game()

	pygame.display.update()

clock.tick(60)

pygame.quit()
import sys, pygame
from pygame import *

size = width, height = [1292, 722]
black = (0, 0, 0)
grey = (128, 128, 128)
other = (238, 165, 0)
testing = font.get_fonts()
testing.sort(key = str.lower)

print(testing)
screen = pygame.display.set_mode(size)
	
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: done=True
	
	screen.fill(black)
	for i in range(0, width, 30):
		for x in range(0, height, 30):
			pygame.draw.rect(screen, other, [i, x, 25, 25])
			#pygame.draw.line(screen, grey, [i + 1, 0], [i + 1, 722], 5)
			#pygame.draw.line(screen, grey, [0, x], [1288, x], 5)
			
	pygame.display.flip()

pygame.quit()
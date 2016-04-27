import sys, pygame
#pygame.init()

size = width, height = [1280, 720]
black = (0, 0, 0)
white = (255, 255, 255)
other = (0, 255, 0)

screen = pygame.display.set_mode(size)
	
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: done=True
	
	screen.fill(black)
	for i in range(4, width, 30):
		for x in range(3, height, 30):
			if i <= width:
				pygame.draw.rect(screen, other, [i, x, 25, 25])
			#	pygame.draw.line(screen, white, [i, 0], [i, 720], 2)
			#	pygame.draw.line(screen, white, [0, x], [1280, x], 2)
			
	pygame.display.flip()

pygame.quit()
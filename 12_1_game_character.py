import pygame
import sys

def run_game():
	#Initializer game, settings and create a screen object
	pygame.init()
	screen_width = 1200
	screen_height = 800
	bg_color = (0, 0, 255)
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Blue Sky")

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#Redraw the screen during each pass through the for loop
		screen.fill(bg_color)

		#Make the most recently drawn screen visible
		pygame.display.flip()




run_game()
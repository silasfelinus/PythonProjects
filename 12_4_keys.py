import pygame
import sys



def run_game():
	#Initializer game, settings and create a screen object
	pygame.init()
	screen_width = 1200
	screen_height = 800
	bg_color = (17, 181, 193)
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Fox")


	while True:

		for event in pygame.event.get():
			#Quit
			if event.type == pygame.QUIT:
				sys.exit()

			#Keydown
			elif event.type == pygame.KEYDOWN:
				print(event.key)

		#Update screen
		screen.fill(bg_color)

		#Make the most recently drawn screen visible
		pygame.display.flip()




run_game()
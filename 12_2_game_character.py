import pygame
import sys

class Fox():

	def __init__(self, screen):
		'''Initialize the ship and set its starting position'''
		self.screen = screen

		#choose ship image
		#chosen_ship = 'ship.bmp'
		fox_image = 'fox.bmp'

		#Load the ship and get its rect.
		self.image = pygame.image.load(fox_image)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

	def blitme(self):
		#Draw the ship at the current location
		self.screen.blit(self.image, self.rect)

def run_game():
	#Initializer game, settings and create a screen object
	pygame.init()
	screen_width = 1200
	screen_height = 800
	bg_color = (17, 181, 193)
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Fox")

	#Make a fox
	fox = Fox(screen)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#Redraw the screen during each pass through the for loop
		screen.fill(bg_color)
		fox.blitme()

		#Make the most recently drawn screen visible
		pygame.display.flip()




run_game()
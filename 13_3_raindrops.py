import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint

class Raindrop(Sprite):
	"""A class to represent a single raindrop"""

	def __init__(self, screen):
		"""Initialize the raindrop and set it's raindropting positon"""
		super(Raindrop, self).__init__()
		self.screen = screen

		#load the raindrop and set its rect attribute"""
		self.image = pygame.image.load('raindrop.bmp')
		self.rect = self.image.get_rect()

		#raindropt each new raindrop near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store the raindrop's exact position
		self.x = float(self.rect.x)

	def blitme(self):
		"""draw the raindrop at its current location"""
		self.screen.blit(self.image, self.rect)



def draw_raindrops(screen, raindrops, screen_width, screen_height):
	"""Calculate the room for raindrops and draw them on the screen"""
	raindrop_height = 50
	raindrop_width = 50

	#Get number of raindrops x
	available_space_x = screen_width - raindrop_width
	number_raindrops_x = int(available_space_x / (2 * raindrop_width))

	# Get the number of rows y
	available_space_y = screen_height - raindrop_height
	number_rows = int(available_space_y / (2 * raindrop_height))


	#Create a raindrop and place it in the row"""
	for row_number in range(number_rows):
		for raindrop_number in range(number_raindrops_x):
			raindrop = Raindrop(screen)
			raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number + randint(-40, 40)
			raindrop.rect.x = raindrop.x
			raindrop.rect.y = raindrop.rect.height + 2 * raindrop.rect.height * row_number + randint(-40, 40)
			raindrops.add(raindrop)


def run_game():
	#Initializer game, settings and create a screen object
	pygame.init()
	screen_width = 1200
	screen_height = 1200
	bg_color = (168, 164, 0)
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Raindrops")
	raindrops = Group()



	draw_raindrops(screen, raindrops, screen_width, screen_height)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


		#Redraw the screen during each pass through the for loop
		screen.fill(bg_color)

		for raindrop in raindrops:
			if randint(0,1) == 1:
				raindrop.rect.y += 1
			if raindrop.rect.bottom > screen_height:
				raindrops.remove(raindrop)
			raindrop.blitme()

		#Make the most recently drawn screen visible
		pygame.display.flip()




run_game()
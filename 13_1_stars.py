import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group

class Star(Sprite):
	"""A class to represent a single star"""

	def __init__(self, screen):
		"""Initialize the star and set it's starting positon"""
		super(Star, self).__init__()
		self.screen = screen

		#load the star and set its rect attribute"""
		self.image = pygame.image.load('star.bmp')
		self.rect = self.image.get_rect()

		#Start each new star near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store the star's exact position
		self.x = float(self.rect.x)

	def blitme(self):
		"""draw the star at its current location"""
		self.screen.blit(self.image, self.rect)



def draw_stars(screen, stars, screen_width, screen_height):
	"""Calculate the room for stars and draw them on the screen"""
	star_height = 50
	star_width = 50

	#Get number of stars x
	available_space_x = screen_width - star_width
	number_stars_x = int(available_space_x / (2 * star_width))

	# Get the number of rows y
	available_space_y = screen_height - star_height
	number_rows = int(available_space_y / (2 * star_height))


	#Create a star and place it in the row"""
	for row_number in range(number_rows):
		for star_number in range(number_stars_x):
			star = Star(screen)
			star.x = star_width + 2 * star_width * star_number
			star.rect.x = star.x
			star.rect.y = star.rect.height + 2 * star.rect.height * row_number
			stars.add(star)


def run_game():
	#Initializer game, settings and create a screen object
	pygame.init()
	screen_width = 1200
	screen_height = 1200
	bg_color = (0, 0, 255)
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Starry Sky")
	stars = Group()

	draw_stars(screen, stars, screen_width, screen_height)

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


		#Redraw the screen during each pass through the for loop
		screen.fill(bg_color)

		for star in stars:
			star.blitme()

		#Make the most recently drawn screen visible
		pygame.display.flip()




run_game()
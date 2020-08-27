import pygame
import sys

class Fox():

	def __init__(self, screen):
		'''Initialize the fox and set its starting position'''
		self.screen = screen

		#ship speed
		self.speed_factor = 1.5

		#choose fox image
		fox_image = 'fox.bmp'

		#Load the fox and get its rect.
		self.image = pygame.image.load(fox_image)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start each new fox at the center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

		#Store decimal values for fox's center
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

		#Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		'''update Fox's position based on the movement flag.'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.speed_factor
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.speed_factor

		#update rect objects from self.center
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery


	def blitme(self):
		#Draw the fox at the current location
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
			#Quit
			if event.type == pygame.QUIT:
				sys.exit()

			#Keydown
			elif event.type == pygame.KEYDOWN:
				#Right
				if event.key == pygame.K_RIGHT:
					fox.moving_right = True
				#Left
				if event.key == pygame.K_LEFT:
					fox.moving_left = True
				#Up
				if event.key == pygame.K_UP:
					fox.moving_up = True
				#Down
				if event.key == pygame.K_DOWN:
					fox.moving_down = True
			#Keyup
			elif event.type == pygame.KEYUP:
				#Right
				if event.key == pygame.K_RIGHT:
					fox.moving_right = False
				#Left
				if event.key == pygame.K_LEFT:
					fox.moving_left = False
				#Up
				if event.key == pygame.K_UP:
					fox.moving_up = False
				#Down
				if event.key == pygame.K_DOWN:
					fox.moving_down = False

		fox.update()

		#Update screen
		screen.fill(bg_color)
		fox.blitme()

		#Make the most recently drawn screen visible
		pygame.display.flip()




run_game()
import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint

class Ship():

	def __init__(self, screen):
		'''Initialize the ship and set its starting position'''
		self.screen = screen
		chosen_ship = 'succubus_small.bmp'

		#Load the ship and get its rect.
		self.image = pygame.image.load('alien_invasion/images/' + chosen_ship)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#Store a decomal value for the ship's center
		self.center = float(self.rect.centerx)

		#Movement flag
		self.moving_right = False
		self.moving_left = False


	def update(self):

		'''update ship's position based on the movement flag.'''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += 1
		if self.moving_left and self.rect.left > 0:
			self.center -= 1

		#Update rect object from self.center
		self.rect.centerx = self.center


	def blitme(self):
		#Draw the ship at the current location
		self.screen.blit(self.image, self.rect)



class Ball(Sprite):
	"""A class to represent a single ball"""

	def __init__(self, screen, screen_width):
		"""Initialize the ball and set it's starting positon"""
		super(Ball, self).__init__()
		self.screen = screen

		#load the ball and set its rect attribute"""
		self.image = pygame.image.load('raindrop.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start each new ball at a random spot on top of the screen
		ball_start_x = randint(0, screen_width)
		self.rect.x = ball_start_x
		self.rect.top = self.screen_rect.top

		#Store the ball's exact position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blitme(self):
		"""draw the ball at its current location"""
		self.screen.blit(self.image, self.rect)



def run_game():
	#Initializer game, settings and create a screen object
	lives = 3
	game_active = True
	pygame.init()

	#Screen Settings
	screen_width = 1200
	screen_height = 1200
	bg_color = (255, 128, 192)
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Catch")

	#Make a ship and ball
	ship = Ship(screen)
	ball = Ball(screen, screen_width)


	#Start the main game loop
	while game_active == True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#Keydown
		if event.type == pygame.KEYDOWN:
			#Right
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			#Left
			if event.key == pygame.K_LEFT:
				ship.moving_left = True
		#Keyup
		elif event.type == pygame.KEYUP:
			#Right
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			#Left
			if event.key == pygame.K_LEFT:
				ship.moving_left = False



		ship.update()

		ball.rect.y += 1
		if (ball.rect.y > screen_height):
			lives -= 1
			if lives == 0:
				game_active = False
			del ball
			ball = Ball(screen, screen_width)
		if  ball.rect.colliderect(ship.rect):
			del ball
			ball = Ball(screen, screen_width)


		#Redraw the screen during each pass through the for loop
		screen.fill(bg_color)

		ball.blitme()
		ship.blitme()

		#Make the most recently drawn screen visible
		pygame.display.flip()






run_game()
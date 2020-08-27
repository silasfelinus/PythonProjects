import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint
import pygame.font

class Button():

	def __init__(self, screen, msg):
		"""Initialize button attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#Set the dimensions and properties of the button
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		#Build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		#The button message needs to be prepped only once
		self.prep_msg(msg)

	def prep_msg(self, msg):
		"""Turn message into a rendered image and center text on the button"""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		#Draw blank button and then draw message
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class Ship():

	def __init__(self, screen):
		'''Initialize the ship and set its starting position'''
		self.screen = screen
		chosen_ship = 'succubus_small.bmp'

		#Load the ship and get its rect.
		self.image = pygame.image.load('alien_invasion/images/' + chosen_ship)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start each new ship at the left center of the screen
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left

		#Store a decomal value for the ship's center
		self.centery = float(self.rect.centery)

		#Movement flag
		self.moving_up = False
		self.moving_down = False

		firing_bullet = False


	def update(self):

		'''update ship's position based on the movement flag.'''
		if self.moving_up and self.rect.top > 0:
			self.centery -= 1
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += 1

		#Update rect object from self.center
		self.rect.centery = int(self.centery)


	def blitme(self):
		#Draw the ship at the current location
		self.screen.blit(self.image, self.rect)





class Ball(Sprite):
	"""A class to represent a single ball"""

	def __init__(self, screen, screen_width, screen_height):
		"""Initialize the ball and set it's starting positon"""
		super(Ball, self).__init__()
		self.screen = screen

		#load the ball and set its rect attribute"""
		self.image = pygame.image.load('raindrop.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start each new ball at the right side of the screen
		self.rect.right = screen_width
		self.rect.y = 0
		#Store the ball's exact position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		#Store speed and going up (positive) or down (negative)
		self.movement_modifier = 1

	def blitme(self):
		"""draw the ball at its current location"""
		self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
	"""A class to manage bullets fired from a ship"""

	def __init__(self, screen, ship, screen_width):
		"""Create a bullet object at current location"""
		super().__init__()
		self.screen = screen
		
		#Create a bullet rect at (0, 0) and set the correct position
		self.rect = pygame.Rect(0, 0, 15,
			10)
		self.rect.centery = ship.rect.centery
		self.rect.right = ship.rect.right

		#Store the bullet's position as a decomal value
		self.x = float(self.rect.x)

		self.color = 60, 60, 60
		self.speed_factor = 6



	def update(self):
		"""Move the bullet up the screen"""
		#Update the decimal position of the bullet
		self.x += self.speed_factor
	
		#Update the rect position
		self.rect.x = int(self.x)

	def draw_bullet(self):
		"""Draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)


def run_game():
	#Initializer game, settings and create a screen object
	lives = 3
	game_active = False
	pygame.init()

	#Screen Settings
	screen_width = 1200
	screen_height = 1200
	bg_color = (255, 128, 192)
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Target Practice")

	#Make the Play button
	play_button = Button(screen, "Play")

	#Make a ship and ball
	ship = Ship(screen)
	ball = Ball(screen, screen_width, screen_height)
	bullet = None
	lives = 3


	#Start the main game loop
	while True:

		#Redraw the screen during each pass through the for loop
		screen.fill(bg_color)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				if play_button.rect.collidepoint(mouse_x, mouse_y):
					button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
					if button_clicked and not game_active:
						#Hide the mouse cursor
						pygame.mouse.set_visible(False)
						"""Start a new game when the player clicks Play"""
						game_active = True
						lives = 3

		if game_active == True:

			#Keydown
			if event.type == pygame.KEYDOWN:
				#Right
				if event.key == pygame.K_UP:
					ship.moving_up = True
				#Left
				if event.key == pygame.K_DOWN:
					ship.moving_down = True
				#Bullet
				if event.key == pygame.K_SPACE and bullet == None:
					bullet = Bullet(screen, ship, screen_width)
			#Keyup
			elif event.type == pygame.KEYUP:
				#Right
				if event.key == pygame.K_UP:
					ship.moving_up = False
				#Left
				if event.key == pygame.K_DOWN:
					ship.moving_down = False



			ship.update()


			#Handle the ball movement
			ball.rect.y += ball.movement_modifier
			if (ball.rect.y > screen_height) or ball.rect.y < 0:
				ball.movement_modifier *= -1

			if bullet:
				bullet.update()
				bullet.draw_bullet()

				#Check for bullet collision
				if ball.rect.colliderect(bullet.rect):
					del ball
					del bullet
					bullet = None
					ball = Ball(screen, screen_width, screen_height)
					lives = 3
				elif bullet.rect.x > screen_width:
					del bullet
					bullet = None
					lives -= 1
					if lives == 0:
						game_active = False
						pygame.mouse.set_visible(True)




			ball.blitme()
			ship.blitme()
		else:
			play_button.draw_button()

		#Make the most recently drawn screen visible
		pygame.display.flip()






run_game()
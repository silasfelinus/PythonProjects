import pygame
from pygame.sprite import Group

"""Game Functions"""
def check_events(ai_settings, screen, ship, bullets):
	'''Respond to key presses and mouse events'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
			
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		#Move ship to the right
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		#Move ship to the right
		ship.moving_left = True
	if event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		#Move ship to the right
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		#Move ship to the right
		ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
	'''Update images on the screen and flip to the new screen'''	

	#Redraw the screen during each pass through the for loop
	screen.fill(ai_settings.bg_color)

	#Redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	#Make the most recently drawn screen visible
	pygame.display.flip()

def update_bullets(bullets):
	"""Update the position of bullets and get rid of old bullets"""
	#Update bullet positions.
	bullets.update()

	#Get rid of bullets that have disappeared
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
	"""fire a bullet if limit hasn't yet been reached"""
	#Create bullet and add to bullet group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)




def run_game():
	#Initializer game, settings and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make a ship
	ship = Ship(ai_settings, screen)
	#Make a group to store bullets
	bullets = Group()


	#Start the main game loop
	while True:

		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)





run_game()
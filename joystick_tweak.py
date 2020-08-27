import pygame

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.JOYBUTTONDOWN:
            print("Button Pressed")
        if j.get_button(6):
            pass
        elif j.get_button(7):
            pass
        elif event.type == pygame.JOYBUTTONUP:
            print("Button Released")


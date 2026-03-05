import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGH = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGH))
pygame.display.set_caption("Adding sounds!")

sound_jump = pygame.mixer.Sound('jump.wav')
sound_jump.set_volume(.25)
sound_jump.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
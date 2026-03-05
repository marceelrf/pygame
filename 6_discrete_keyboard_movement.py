import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGH = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGH))
pygame.display.set_caption("Keyboards Movements")

VELOCITY = 1

ave_image = pygame.image.load('image001.png')
ave_rect = ave_image.get_rect()
ave_rect.centerx = WINDOW_WIDTH//2
ave_rect.bottom = WINDOW_HEIGH

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            ave_rect.x -= VELOCITY
        if event.key == pygame.K_RIGHT:
            ave_rect.x += VELOCITY
        if event.key == pygame.K_UP:
            ave_rect.y -= VELOCITY
        if event.key == pygame.K_DOWN:
            ave_rect.y += VELOCITY
    
    display_surface.fill((0,0,0))
    display_surface.blit(ave_image, ave_rect)
    
    pygame.display.update()
            
pygame.quit()
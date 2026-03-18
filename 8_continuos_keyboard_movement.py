import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGH = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGH))
pygame.display.set_caption("Continuos Movement!")

#Set FDS and Clock
FPS = 30
clock = pygame.time.Clock()

VELOCITY = 5

ave_image = pygame.image.load('image001.png')
ave_rect = ave_image.get_rect()
ave_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGH//2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get a list of all keys currently being held
    keys = pygame.key.get_pressed()
    
    # print(keys)
    
    if keys[pygame.K_LEFT]:
        ave_rect.x -= VELOCITY
        
    if keys[pygame.K_RIGHT]:
        ave_rect.x += VELOCITY
        
    if keys[pygame.K_UP]:
        ave_rect.y -= VELOCITY
    
    if keys[pygame.K_DOWN]:
        ave_rect.y += VELOCITY
    
    display_surface.fill((0,0,0))
    display_surface.blit(ave_image, ave_rect)
    
    pygame.display.update()
    
    clock.tick(FPS)
            
pygame.quit()
import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGH = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGH))
pygame.display.set_caption("Restricted Movement!")

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
    
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and ave_rect.left > 0:
        ave_rect.x -= VELOCITY
        
    if (keys[pygame.K_RIGHT]  or keys[pygame.K_d]) and ave_rect.right < WINDOW_WIDTH:
        ave_rect.x += VELOCITY
        
    if (keys[pygame.K_UP]  or keys[pygame.K_w]) and ave_rect.top > 0:
        ave_rect.y -= VELOCITY
    
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and ave_rect.bottom < WINDOW_HEIGH:
        ave_rect.y += VELOCITY
    
    display_surface.fill((0,0,0))
    display_surface.blit(ave_image, ave_rect)
    
    pygame.display.update()
    
    clock.tick(FPS)
            
pygame.quit()
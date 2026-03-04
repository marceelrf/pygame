import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGH = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGH))
pygame.display.set_caption("Blitting Images!")

bird_image = pygame.image.load("image001.png")
bird_rect = bird_image.get_rect()
bird_rect.topleft = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display_surface.blit(bird_image, bird_rect) 
    
    pygame.draw.line(display_surface, (255,255,255), (0, 75), (WINDOW_WIDTH, 75), 5)
    
    pygame.display.update()
        
pygame.quit()
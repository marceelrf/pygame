import pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGH = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGH))
pygame.display.set_caption("Mouse movents!")

ave_image = pygame.image.load('image001.png')
ave_rect = ave_image.get_rect()
ave_rect.topleft = (25, 25)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print(event)
        #     mouse_x = event.pos[0]
        #     mouse_y = event.pos[1]
        #     ave_rect.centerx = mouse_x
        #     ave_rect.centery = mouse_y
            
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            ave_rect.centerx = mouse_x
            ave_rect.centery = mouse_y
             
    display_surface.fill((0,0,0))
    display_surface.blit(ave_image, ave_rect)
    pygame.display.update()
            

pygame.quit()
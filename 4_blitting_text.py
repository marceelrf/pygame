import pygame


pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGH = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGH))
pygame.display.set_caption("Blitting Images!")

GREEN = (0 , 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

# See all availabre system fonts
# fonts = pygame.font.get_fonts()
# for font in fonts:
#     print(font)

system_font = pygame.font.SysFont("calibri", 64)
custon_font = pygame.font.Font("whoa-font\Whoa-p3ar.ttf", 32)

#define text
system_text = system_font.render("Dragons Rule!", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGH//2)

custon_text = custon_font.render("Move the dragon soon!", True, GREEN)
custon_text_rect = custon_text.get_rect()
custon_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGH//2 + 100)

runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
            
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custon_text, custon_text_rect)
    
    pygame.display.update()
            
pygame.quit()
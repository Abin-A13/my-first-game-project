import pygame

pygame.init()
sienna = (160, 82, 45)
display_width = 1200
display_height = 700
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("ABY's Car Game")
clock = pygame.time.Clock()

def game_loop():
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True

                gamedisplays.fill(sienna)
                pygame.display.update()
                clock.tick(60)
game_loop()
pygame.quit()
quit()


import pygame

pygame.init()
grey = (119, 118, 110)
display_width = 1366
display_height = 700
displays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("ABBYY's Car Game")
clock = pygame.time.Clock()
caring = pygame.image.load("images.jpeg")
backgroundpic = pygame.image.load("images (1).jpeg")


def background():
    displays.blit(backgroundpic, (0,700))
    displays.blit(backgroundpic, (700, 0))


def car(x, y):
    displays.blit(caring, (x, y))


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    xchange = 0
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -5
            if event.key == pygame.K_RIGHT:
                xchange = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                continue
            xchange = 0
        x += xchange
        displays.fill(grey)
        background()
        car(x, y)
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()

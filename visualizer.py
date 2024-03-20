import pygame
from items import items

pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()
running = True
surface = pygame.Surface((128, 128))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pixels = pygame.PixelArray(surface)

    for x in range(128):
        for y in range(128):
            pixels[x, y] = items[0][x // 8][y // 8]

    pixels.close()

    display = pygame.display.set_mode((128, 128))
    display.blit(surface, (0, 0))

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
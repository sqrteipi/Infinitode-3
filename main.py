import pygame

pygame.init()

# FULL SCREEN
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
GRID_SIZE = 25
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pixels = pygame.PixelArray(surface)

    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            if ((x + y) & 1) == 0:
                pixels[x:x+GRID_SIZE, y:y+GRID_SIZE] = (64, 64, 64)
            else:
                pixels[x:x+GRID_SIZE, y:y+GRID_SIZE] = (192, 192, 192)

    pixels.close()

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display.blit(surface, (0, 0))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
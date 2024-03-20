import pygame

pygame.init()

# FULL SCREEN
GRID_SIZE = 64
SCREEN_WIDTH = 1920 // GRID_SIZE * GRID_SIZE
SCREEN_HEIGHT = 1080 // GRID_SIZE * GRID_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pixels = pygame.PixelArray(surface)

    oddity = True
    for x in range(0, SCREEN_WIDTH+1, GRID_SIZE):
        for y in range(0, SCREEN_HEIGHT+1, GRID_SIZE):
            if oddity:
                pixels[x:x+GRID_SIZE, y:y+GRID_SIZE] = (64, 64, 64)
            else:
                pixels[x:x+GRID_SIZE, y:y+GRID_SIZE] = (192, 192, 192)
            oddity = not oddity

    pixels.close()

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display.blit(surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
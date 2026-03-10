import pygame


pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 255)

WIDTH, HEIGHT = 800, 800
TILESIZE = 20

GRID_WIDTH = WIDTH // TILESIZE
GRID_HEIGHT = HEIGHT // TILESIZE
FPS = 60

screen =pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_grid(positions):
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK,(0,row*TILESIZE),(WIDTH,row*TILESIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col*TILESIZE, 0), (col * TILESIZE, HEIGHT))

def main():
    running = True




    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        positions = set()

        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
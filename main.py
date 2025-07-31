import pygame
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
)


def main() -> None:
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    game_window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    flags = pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE
    screen = pygame.display.set_mode(game_window_size, flags, vsync=1)
    colour = pygame.Color(0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(colour)
        pygame.display.flip()

        dt = (clock.tick(60) / 1000)


if __name__ == "__main__":
    main()

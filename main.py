import pygame
from player import Player
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    PLAYER_RADIUS,
)


def main() -> None:
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    game_window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(game_window_size, vsync=1)
    colour = pygame.Color(0, 0, 0)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        screen.fill(colour)
        # print(f"Player position: {player.position}, radius: {PLAYER_RADIUS}")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()

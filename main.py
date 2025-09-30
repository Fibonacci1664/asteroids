import pygame
import sys

from player import Player
from shot import Shot
from asteroidfield import AsteroidField
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


def main() -> None:
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0

    game_window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(game_window_size, vsync=1)
    pygame.display.set_caption("Asteroids")
    colour = pygame.Color(0, 0, 0)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable: pygame.sprite.Group = pygame.sprite.Group()
    drawable: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    shots: pygame.sprite.Group = pygame.sprite.Group()

    player = Player(x, y, [updatable, drawable], shots)
    _ = AsteroidField([updatable, drawable, asteroids])

    # Player.containers = (updatable, drawable)
    # Asteroid.containers = (updatable, drawable, asteroids)
    # AsteroidField.containers = updatable

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        screen.fill(colour)
        # print(f"Player position: {player.position}, radius: {PLAYER_RADIUS}")
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                print(type(next(iter(shots))))
                print(isinstance(shot, Shot))
                if shot.has_collided(asteroid):
                    asteroid.kill()
                    shot.kill()

            if player.has_collided(asteroid):
                print("Game over!")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()

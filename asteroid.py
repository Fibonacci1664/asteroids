import pygame

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(
        self, x: float, y: float, radius: float, container_list: list
    ) -> None:
        super().__init__(x, y, radius, container_list)

    def draw(self, screen: pygame.Surface) -> None:
        yellow = (255, 255, 0)
        line_width = 2

        pygame.draw.circle(
            screen, yellow, self.position, self.radius, line_width
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

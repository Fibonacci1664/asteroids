import pygame

from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(
        self, x: float, y: float, SHOT_RADIUS: float, container_list: list
    ) -> None:
        super().__init__(x, y, SHOT_RADIUS, container_list)
        self.SHOT_RADIUS = SHOT_RADIUS

    def draw(self, screen: pygame.Surface) -> None:
        red = (255, 0, 0)
        line_width = 2

        pygame.draw.circle(
            screen, red, self.position, self.SHOT_RADIUS, line_width
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

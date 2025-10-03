import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(
        self, x: float, y: float, radius: float, container_list: list
    ) -> None:
        super().__init__(x, y, radius, container_list)

        self.container_list: list = container_list

    def draw(self, screen: pygame.Surface) -> None:
        yellow = (255, 255, 0)
        line_width = 2

        pygame.draw.circle(
            screen, yellow, self.position, self.radius, line_width
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rand_angle = random.uniform(20, 50)
        pos_vel_vec = self.velocity.rotate(rand_angle)
        neg_vel_vec = self.velocity.rotate(-rand_angle)
        new_asteroid_rad = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(
            self.position.x,
            self.position.y,
            new_asteroid_rad,
            self.container_list,
        )

        asteroid_1.velocity = pos_vel_vec * 1.2

        asteroid_2 = Asteroid(
            self.position.x,
            self.position.y,
            new_asteroid_rad,
            self.container_list,
        )

        asteroid_2.velocity = neg_vel_vec * 1.2

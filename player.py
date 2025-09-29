import pygame

from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    SHOT_RADIUS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(
        self,
        x: float,
        y: float,
        container_list: list,
        shots_group: pygame.sprite.Group,
    ) -> None:
        super().__init__(
            x,
            y,
            PLAYER_RADIUS,
            container_list,
        )
        self.rotation: float = 0
        self.shots_group = shots_group
        self.container_list = container_list

        # For controlling the rate of fire
        self.time_until_next_shot = 0.0  # countdown timer intialisation

    def triangle(self) -> list:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        )
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        white = (255, 255, 255)
        # print(f"Drawing triangle at: {self.triangle()}")
        pygame.draw.polygon(screen, white, self.triangle(), 2)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        self.time_until_next_shot = max(0.0, self.time_until_next_shot - dt)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.time_until_next_shot <= 0.0:
            self.shoot()
            self.time_until_next_shot = PLAYER_SHOOT_COOLDOWN

    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self) -> None:
        # Spawn a new shot at the players position
        position = pygame.Vector2(self.position)
        velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        )
        shot = Shot(
            position.x,
            position.y,
            SHOT_RADIUS,
            [self.container_list[0], self.container_list[1], self.shots_group],
        )
        shot.velocity = velocity

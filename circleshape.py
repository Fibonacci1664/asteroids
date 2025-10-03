import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(
        self, x: float, y: float, radius: float, containers: list
    ) -> None:
        # if hasattr(self, "containers"):
        super().__init__(*containers)
        # else:
        # super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen: pygame.Surface) -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    # CircleShape in quotes is a fwd ref, basically "trust me bro!"
    def has_collided(self, object: "CircleShape") -> bool:
        r1 = self.radius
        r2 = object.radius
        distance = self.position.distance_to(object.position)

        if distance <= (r1 + r2):
            return True
        return False

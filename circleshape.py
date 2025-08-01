import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        

        self.position = pygame.Vector2(x, y)
        self.position = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass
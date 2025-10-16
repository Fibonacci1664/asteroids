import pygame
from gui.guiaction import GUIAction
from inputservice import InputService


class TitleScreen:
    # Simple title GUI with a "Play" button
    def __init__(self, screen_size: tuple) -> None:
        width, height = screen_size

        # Basic font
        self.title_font = pygame.font.SysFont(None, 64)
        self.button_font = pygame.font.SysFont(None, 32)

        # Centered button rect
        btn_width = 240
        btn_height = 60
        self.button_rect = pygame.Rect(
            (width - btn_width) // 2, (height // 2), btn_width, btn_height
        )

    def update(self, input_service: InputService) -> GUIAction:
        # Query current mouse position for hover and click tests

        mx, my = pygame.mouse.get_pos()
        hovered = self.button_rect.collidepoint(mx, my)

        # Scan this frame#s events for a button release over the Play button
        for e in input_service.events:
            if (
                e.type == pygame.MOUSEBUTTONUP
                and hovered
                and input_service.mouse_up_since_transition
            ):
                # Signal that the GUI requests to start game
                return GUIAction.START_GAME

        return GUIAction.NONE

    def draw(self, surface: pygame.Surface) -> None:
        # Fill a dark background for the title screen
        surface.fill((10, 10, 20))

        # Render and centre the title test
        title = self.title_font.render("Asteroids", True, (200, 200, 240))
        surface.blit(
            title,
            title.get_rect(
                center=(surface.get_width() // 2, surface.get_height() // 3)
            ),
        )

        # Draw the Play button; change colour on hover
        mx, my = pygame.mouse.get_pos()
        hovered = self.button_rect.collidepoint(mx, my)
        colour = (80, 160, 80) if hovered else (60, 120, 60)
        pygame.draw.rect(surface, colour, self.button_rect, border_radius=8)

        # Draw the button label centered inside the rect
        label = self.button_font.render("Play", True, (20, 20, 20))
        surface.blit(label, label.get_rect(center=self.button_rect.center))

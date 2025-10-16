import pygame
from gui.guiaction import GUIAction
from gui.titlescreen import TitleScreen
from inputservice import InputService


class GUIManager:
    # Holds a single active screen (Title, Gameover etc). If None, GUI is idle
    def __init__(self) -> None:
        self.active_screen = None

    def set_screen(self, screen_or_none: TitleScreen | None) -> None:
        # Swap active GUI screen on state change
        self.active_screen = screen_or_none

    def update(self, input_service: InputService) -> GUIAction:
        # Let the active screen process input and return an action
        if not self.active_screen:
            return GUIAction.NONE
        return self.active_screen.update(input_service)

    def draw(self, surface: pygame.Surface) -> None:
        # Draw the active screen last so it appears on top
        if self.active_screen:
            self.active_screen.draw(surface)

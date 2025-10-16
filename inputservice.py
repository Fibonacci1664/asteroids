import pygame


class InputService:
    def __init__(self) -> None:
        self.events = []  # Raw pygame events collected this frame

        # Prevent clicks leaking from title to gameplay
        self.mouse_up_since_transition = False

    def poll(self) -> None:
        # Pull all input events once per frame
        self.events = pygame.event.get()

        # Detect MOUSEBUTTONUP for the title "Play" logic
        for e in self.events:
            if e.type == pygame.MOUSEBUTTONUP:
                self.mouse_up_since_transition = True

    def consume_all(self) -> None:
        # Clear buffered events
        self.events.clear()

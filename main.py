import pygame
import sys

from player import Player
from asteroidfield import AsteroidField
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)

from statemanager import GameState, StateManager
from inputservice import InputService
from gui.guimanager import GUIManager
from gui.guiaction import GUIAction
from gui.titlescreen import TitleScreen


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

    def build_world() -> Player:
        # Rebuild gameplay entities for a clean slate on newgame
        updatable.empty()
        drawable.empty()
        asteroids.empty()
        shots.empty()
        player = Player(x, y, [updatable, drawable], shots)
        _ = AsteroidField([updatable, drawable, asteroids])
        return player

    # Create an initial gameplay world, this wont update while in TITLE
    player = build_world()

    # Managers
    state = StateManager()  # Controls TITLE/PLAYING
    input_service = InputService()  # Polls events once per frame
    gui = GUIManager()  # Runs current GUI screen
    gui.set_screen(TitleScreen(game_window_size))

    # Require a fresh mouse button release after entering TITLE
    input_service.mouse_up_since_transition = False

    while True:
        # Collect all input events exactly once this frame
        input_service.poll()

        # Handle window close regardless of state
        for event in input_service.events:
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        if state.get_state() == GameState.TITLE:
            # Let GUI process input, possibly requesting state changes
            action = gui.update(input_service)

            # Draw the title screen (bg + button)
            gui.draw(screen)

            # If Play clicked and mouse up after entering TITLE, start game
            if (
                action == GUIAction.START_GAME
                and input_service.mouse_up_since_transition
            ):
                player = build_world()
                state.set_state(GameState.PLAYING)
                input_service.consume_all()
                gui.set_screen(None)
        elif state.get_state() == GameState.PLAYING:
            # Clear the screen for gameplay rendering
            screen.fill(colour)

            updatable.update(dt)

            for asteroid in asteroids:
                for shot in shots:
                    if shot.has_collided(asteroid):
                        asteroid.split()
                        shot.kill()

                if player.has_collided(asteroid):
                    print("Game over!")
                    sys.exit()

            for sprite in drawable:
                sprite.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()

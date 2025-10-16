from enum import (
    Enum,
    auto,
)  # Enum gives named constants; auto() assigns unique values


class GameState(Enum):
    TITLE = auto()
    PLAYING = auto()


class StateManager:
    def __init__(self) -> None:
        self._state = GameState.TITLE  # Initial state

    def get_state(self) -> GameState:
        return self._state

    def set_state(self, new_state: GameState) -> None:
        self._state = new_state

from enum import Enum, auto


class GUIAction(Enum):
    # Minimal "intent" signals from GUI to Game
    NONE = auto()
    START_GAME = auto()

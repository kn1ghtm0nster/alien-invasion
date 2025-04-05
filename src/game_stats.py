"""
Module contains the GameStats class.
"""


class GameStats:
    """
    Track statistics for Alien Invasion.
    """

    def __init__(self, ai_game):
        """
        Initialize statistics.
        """
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active status
        self.game_active = True

    def reset_stats(self) -> None:
        """
        Initialize statistics that can change during the game.
        """
        self.ships_left = self.settings.ship_limit

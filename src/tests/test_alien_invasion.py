from src.alien_invasion import AlienInvasion

import os
import unittest
from dotenv import load_dotenv

load_dotenv()

# hiding the pygame support prompt to create less clutter in terminal when
# running tests.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = os.environ.get(
    'PYGAME_HIDE_SUPPORT_PROMPT', 'hide')


class TestAlienInvasion(unittest.TestCase):
    """
    Class to test base functionality of the AlienInvasion class.
    """

    def setUp(self):
        """
        Create an instance of `AlienInvasion` for testing.
        """
        self.game = AlienInvasion()

    def test_ship_starting_position(self):
        """
        Verify that the ship starts at the correct position.
        """
        screen_rect = self.game.screen.get_rect()

        # Assert that the ship's starting position is the bottom center of the screen.
        self.assertEqual(self.game.ship.rect.midbottom,
                         (screen_rect.centerx, screen_rect.bottom))

    def test_ship_moving_right(self):
        """
        Check that moving the ship to the right works.
        """
        self.game.ship.moving_right = True
        self.assertTrue(self.game.ship.moving_right)

    def test_moving_left(self):
        """
        Check that moving the ship to the left works.
        """
        self.game.ship.moving_left = True
        self.assertTrue(self.game.ship.moving_left)

    def test_fire_bullet_limit(self):
        """
        Ensure that only THREE bullets are allowed on the screen at a time.
        """
        for _ in range(5):
            self.game._fire_bullet()
        self.assertLessEqual(len(self.game.bullets),
                             self.game.settings.bullets_allowed)


if __name__ == '__main__':
    unittest.main()

from src.alien_invasion import AlienInvasion
from src.ship import Ship

import os
import pygame
import unittest
from dotenv import load_dotenv

load_dotenv()

# hiding the pygame support prompt to create less clutter in terminal when
# running tests.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = os.environ.get(
    'PYGAME_HIDE_SUPPORT_PROMPT', 'hide')


class TestShip(unittest.TestCase):
    """
    Tests for the `Ship` class.
    """

    def setUp(self):
        """
        Create a test instance of `AlienInvasion` and a `Ship`
        instance for each test.
        """
        pygame.init()
        self.game = AlienInvasion()
        self.ship = self.game.ship

    def test_initial_position(self):
        """
        Verify the ship starts at the bottom center of the screen.
        """
        self.assertEqual(self.ship.rect.midbottom,
                         self.game.screen.get_rect().midbottom)

    def test_move_right_flag(self):
        """
        Ensure moving_right is honored during the update() method.
        """
        self.ship.moving_right = True
        old_x = self.ship.x
        self.ship.update()
        self.assertGreater(self.ship.x, old_x)

    def test_move_left_flag(self):
        """
        Ensure moving_left is honored during the update() method.
        """
        self.ship.moving_left = True
        old_x = self.ship.x
        self.ship.update()
        self.assertLess(self.ship.x, old_x)

    def test_bound_right(self):
        """
        Ensure the ship does NOT move beyond the right edge of the screen.
        """
        screen_right = self.game.screen.get_rect().right
        self.ship.rect.right = screen_right
        self.ship.x = float(self.ship.rect.x)
        self.ship.moving_right = True
        self.ship.update()
        self.assertEqual(self.ship.rect.right, screen_right)

    def test_bound_left(self):
        """
        Ensure the ship does not move beyond the left edge of the screen.
        """
        self.ship.rect.left = 0
        self.ship.x = float(self.ship.rect.x)
        self.ship.moving_left = True
        self.ship.update()
        self.assertEqual(self.ship.rect.left, 0)


if __name__ == '__main__':
    unittest.main()

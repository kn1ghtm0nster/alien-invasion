from src.alien_invasion import AlienInvasion
from src.bullet import Bullet

import os
import pygame
import unittest
from dotenv import load_dotenv

load_dotenv()

# hiding the pygame support prompt to create less clutter in terminal when
# running tests.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = os.environ.get(
    'PYGAME_HIDE_SUPPORT_PROMPT', 'hide')


class TestBullet(unittest.TestCase):
    """
    Test the `Bullet` class.
    """

    def setUp(self):
        """
        Create a test instance of `AlienInvasion` and a `Bullet` 
        instance for each test.
        """
        pygame.init()
        self.game = AlienInvasion()
        self.bullet = Bullet(self.game)

    def test_bullet_starting_position(self):
        """
        Verify that the bullet starts at the ship's midtop position
        and that the bullet's y attribute matches its rect y coordinate.
        """
        self.assertEqual(self.bullet.rect.midtop, self.game.ship.rect.midtop)
        self.assertAlmostEqual(self.bullet.y, float(self.bullet.rect.y))

    def test_bullet_moves_up(self):
        """
        Ensure that the bullet sprite moves up the screen after update()
        method is called.
        """
        initial_y = self.bullet.y
        self.bullet.update()
        self.assertLess(self.bullet.y, initial_y)


if __name__ == '__main__':
    unittest.main()

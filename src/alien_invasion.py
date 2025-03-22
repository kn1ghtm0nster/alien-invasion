import sys
import pygame
from pygame.event import Event

from .settings import Settings
from .ship import Ship
from .bullet import Bullet


class AlienInvasion:
    """
    Overall class to maange game assets and behavior.
    """

    def __init__(self):
        """
        Initialize the game, and create game resources.
        """
        pygame.init()
        self.settings = Settings()

        # use the code below if you want to run the game in a window.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # use the code below if you want to run the game in fullscreen mode.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def _check_events(self) -> None:
        """
        Respond to key presses and mouse events.
        """
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: Event) -> None:
        """
        Respond to key presses.

        :param event: The event to check.
        :type event: Event
        :return: None
        """
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right until the key is released.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left until the key is released.
            self.ship.moving_left = True

        # this keyboard shortcut helps with exiting game in fullscreen mode.
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event: Event) -> None:
        """
        Respond to key releases.

        :param event: The event to check.
        :type event: Event
        :return: None
        """
        if event.key == pygame.K_RIGHT:
            # Stop moving the ship to the right.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stop moving the ship to the left.
            self.ship.moving_left = False

    def _fire_bullet(self) -> None:
        """
        Create a new bullet and add it to the bullets group.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) -> None:
        """
        Update position of bullets and get rid of old bullets.
        """
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self) -> None:
        """
        Update images on the screen, and flip to the new screen.
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self) -> None:
        """
        Start the main loop for the game.
        """
        while True:
            self._check_events()

            self.ship.update()
            self._update_bullets()

            # Redraw the screen during each pass through the
            # loop.
            self._update_screen()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

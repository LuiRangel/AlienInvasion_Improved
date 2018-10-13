import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien UFO in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image and set its rect attribute
        self.images = []

        self.images.append(pygame.image.load('images/alien_f1.gif'))
        self.images.append(pygame.image.load('images/alien_f1.gif'))
        self.images.append(pygame.image.load('images/alien_f1.gif'))
        self.images.append(pygame.image.load('images/alien_f1.gif'))
        self.images.append(pygame.image.load('images/alien_f1.gif'))
        self.images.append(pygame.image.load('images/alien_f1.gif'))
        self.images.append(pygame.image.load('images/alien_f2.gif'))
        self.images.append(pygame.image.load('images/alien_f2.gif'))
        self.images.append(pygame.image.load('images/alien_f2.gif'))
        self.images.append(pygame.image.load('images/alien_f2.gif'))
        self.images.append(pygame.image.load('images/alien_f2.gif'))
        self.images.append(pygame.image.load('images/alien_f2.gif'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)


class AlienAlpha(Sprite):
    """A class to represent a alien type alpha in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(AlienAlpha, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image and set its rect attribute
        self.images = []

        self.images.append(pygame.image.load('images/alien_alpha_f1.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f1.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f1.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f1.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f1.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f1.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f2.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f2.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f2.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f2.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f2.gif'))
        self.images.append(pygame.image.load('images/alien_alpha_f2.gif'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)


class AlienScouter(Sprite):
    """A class to represent a single alien scouter in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(AlienScouter, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.points = 20

        # load the alien image and set its rect attribute
        self.images = []

        self.images.append(pygame.image.load('images/alien_scouter_f1.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f1.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f1.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f1.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f1.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f1.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f2.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f2.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f2.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f2.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f2.gif'))
        self.images.append(pygame.image.load('images/alien_scouter_f2.gif'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

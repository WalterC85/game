import sys
import pygame
from settings import Settings
from ship import Ship 

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
         # initializes the background settings that Pygame needs to work properly
        pygame.init()
        self.settings = Settings()
        # create a display window, on which we’ll draw all the game’s graphical ele­ ments.
        # The argument (1200, 800) is a tuple that defines the dimensions of the game window, which will be 1200 pixels wide by 800 pixels high
        # The object we assigned to self.screen is called a surface. 
        # A surface in Pygame is a part of the screen where a game element can be displayed.
        # Each element in the game, like an alien or a ship, is its own surface. 
        # The surface returned by display.set_mode() represents the entire game window. 
        # When we activate the game’s animation loop, this surface will be redrawn on every pass through the loop, so it can be updated with any changes trig­ gered by user input.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # Set the background color to gray
        #self.bg_color = (230, 230, 230) # removed because defined in settings class


        # method to controll the game
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            # Watch for keyboard and mouse events.
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                

    def _check_keydown_events(self, event):
        """Respond to keypress event """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """Respond to keyrelease event """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #     elif event.type == pygame.KEYDOWN: 
        #         if event.key == pygame.K_RIGHT:
        #             # Move the ship to the right.
        #             self.ship.rect.x += 1
    
    def _update_screen(self):
            """Update images on the screen, and flip to the new screen."""
            # Redraw the screen during each pass through the loop.
            # fill the screen with the background color using the fill() method, 
            # which acts on a surface and takes only one argument: a color.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            # tells Pygame to make the most recently drawn screen visible. 
            # In this case, it simply draws an empty screen on each pass through the while loop, erasing the old screen so only the new screen is visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

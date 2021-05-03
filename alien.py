import sys
import pygame
from settings import Settings
from ship import Ship 
class Aleininvation:
    """this is my first class in alein invation"""
    def __init__(self):
        """initialize the function"""
        pygame.init()
        self.settings = Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("alien invation")
        self.bg_color = self.settings.bg_color
        self.ship=Ship(self)
    def run_game(self):
        """start the game """
        while True:
            self._check_events()
    def _check_events(self):
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            pygame.display.flip()
if __name__=='__main__':
    ai=Aleininvation()
    ai.run_game()
    

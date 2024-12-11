import pygame

from assets import initialize_assets, get_asset_library

class KnightGame:
    def __init__(self, DISPLAY_SIZE, FLAGS = pygame.RESIZABLE):
        
        pygame.init()
        
        self.window = pygame.display.set_mode(DISPLAY_SIZE, FLAGS)
        self.clock = pygame.time.Clock()
        self.gameloop = True
        
        
          

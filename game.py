import pygame
from assets import initialize_assets
from button import Button

class KnightGame:
    def __init__(self, DISPLAY_SIZE):
        
        pygame.init()
        
        self.window = pygame.display.set_mode(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()
        self.program_running = True
        self.current_loop = "Game"
        self.game_state = None
        
        self.asset_library = initialize_assets()
        
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.program_running = False
                
    def menu(self):
        while self.program_running and self.current_loop == "Menu":
            # --Delta Time and Events--
            dt = self.clock.tick(60)
            self.event_handler()
            
            
            pygame.display.flip()
            
    def game(self):
        knight = self.asset_library["knight"]
        buttonTest = Button(self.window, pygame.Vector2(pygame.display.get_surface().get_width() // 2, pygame.display.get_surface().get_height() // 2))
        while self.program_running and self.current_loop == "Game":
            # --Delta Time and Events--
            dt = self.clock.tick(60)
            self.event_handler()

            # --Display--
            self.window.blit(knight, (0, 0))
            self.window.blit(knight, ((pygame.display.get_surface().get_width() / 6) * 1, (pygame.display.get_surface().get_height() / 6) * 1))
            self.window.blit(knight, ((pygame.display.get_surface().get_width() / 6) * 2, (pygame.display.get_surface().get_height() / 6) * 2))
            self.window.blit(knight, ((pygame.display.get_surface().get_width() / 6) * 3, (pygame.display.get_surface().get_height() / 6) * 3))
            self.window.blit(knight, ((pygame.display.get_surface().get_width() / 6) * 4, (pygame.display.get_surface().get_height() / 6) * 4))
            self.window.blit(knight, ((pygame.display.get_surface().get_width() / 6) * 5, (pygame.display.get_surface().get_height() / 6) * 5))
            buttonTest.display_button()
            
            pygame.display.flip()
            
    
    def run(self):
        while self.program_running:
            if self.current_loop == "Menu":
                self.menu()
            elif self.current_loop == "Game":
                self.game()
        
        pygame.quit()
            
        
        

          

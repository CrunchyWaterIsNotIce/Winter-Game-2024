import pygame as pg

class Menu:
    def __init__(self):
        pass
    
    # def start(self):
    #     """Initialization logic for the menu."""
    #     print("Entered Menu State")

    def update(self):
        """Handle menu logic."""
        # Example: Transition to Game state
        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:  # Press Enter to start game
            return "GAME"

    def draw(self, screen):
        """Draw the menu."""
        screen.fill("yellow")
        print('a')

class Game:
    def __init__(self):
        pass
    def start(self):
        """Initialization logic for the game."""
        print("Entered Game State")

    def update(self):
        """Game logic."""
        # Example: Transition to Win state
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:  # Press W to win
            return "WIN"

    def draw(self, screen):
        """Draw the game."""
        font = pg.font.Font(None, 50)
        text = font.render("Game: Press W to Win", True, (255, 255, 255))
        screen.blit(text, (200, 350))

class Win:
    def __init__(self):
        pass
    def start(self):
        """Initialization logic for the win screen."""
        print("Entered Win State")

    def update(self):
        """Win logic."""
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:  # Press Esc to return to menu
            return "MENU"

    def draw(self, screen):
        """Draw the win screen."""
        font = pg.font.Font(None, 50)
        text = font.render("You Win! Press Esc to Menu", True, (255, 255, 255))
        screen.blit(text, (150, 350))

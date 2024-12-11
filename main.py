import pygame

from game import KnightGame

def initializeGame():
    game = KnightGame((400, 400), pygame.FULLSCREEN)
    # game.initalize_assets()

if __name__ == "__main__":
    initializeGame()
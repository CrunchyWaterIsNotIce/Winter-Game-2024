import pygame

from game import KnightGame

def initializeGame():
    game = KnightGame((770, 770))
    game.run()

if __name__ == "__main__":
    initializeGame()
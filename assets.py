import pygame, os

image_library = {}

knight_path = os.path.join("assets", "Knight_demo.png")

def initialize_assets():
    image_library["knight"] = pygame.transform.scale(pygame.image.load(knight_path), (128, 128)).convert_alpha()
    # pygame.image.load(knight_path).convert_alpha()
    
    return image_library
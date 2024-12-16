import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
RECT_WIDTH, RECT_HEIGHT = 200, 100
FPS = 60

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hover Effect Example")

# Rectangle setup
rect_x = (SCREEN_WIDTH - RECT_WIDTH) // 2
rect_y = (SCREEN_HEIGHT - RECT_HEIGHT) // 2
rect = pygame.Rect(rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)

# Clock
clock = pygame.time.Clock()

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Save the old position
    old_rect = rect.copy()

    # Determine if mouse is over the rectangle
    if rect.collidepoint(mouse_pos):
        color = GREEN
        rect.centerx += 5  # Move the rectangle
    else:
        color = RED

    # Clear the old rectangle area
    screen.fill(BLACK, old_rect)

    # Draw the rectangle at the new position
    pygame.draw.rect(screen, color, rect)

    # Update both old and new areas
    pygame.display.update([old_rect, rect])

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()

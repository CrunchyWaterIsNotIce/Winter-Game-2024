import pygame

class Button:
    def __init__(self, surface, center_pos, img = None):
        self.surface = surface
        self.center = center_pos
        self.icon = img
        if img == None:
            self.size = (50, 50)
        else:
            self.size = img.get_size()
        self.isSelected = False
        
    

    def display_button(self, mouse_pos):
        self.hover(mouse_pos)
        if self.icon == None:
            rectTest = pygame.Rect(self.center[0] - (self.size[0] // 2), self.center[1] - (self.size[1] // 2), self.size[0], self.size[1])
            if self.isSelected:
                color = "green"
            else:
                color = "red"
            pygame.draw.rect(self.surface, color, rectTest)
        else:
            self.surface.blit(self.icon, (self.center[0] - (self.size[0] // 2), self.center[1] - (self.size[1] // 2)))

    
    
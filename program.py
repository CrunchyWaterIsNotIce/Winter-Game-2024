import pygame as pg
from math import sin

'''
    Where the majority of how the game logic and its components.
'''

# Game Components
class Button(pg.sprite.Sprite):
    def __init__(self, group, center_pos, distance = 20, direction = (-1, -1)):
        super().__init__(group)
        
        #FOR DIRECTION: Upper Left -> (-1, -1), Middle = (0,0), Lower Right -> (1, 1)
        
        self.image = pg.Surface([64, 64])
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = center_pos
        
        self.anchor_pos = center_pos
        hover_direction = tuple(distance * i for i in direction)
        self.hover_pos = (hover_direction[0] + self.rect.centerx, hover_direction[1] + self.rect.centery)
        
        self.target_pos = self.hover_pos
        
        self.selected = False
        self.done = True
        self.delay = False
        
    def hover(self):
        '''
        EDGE CASE MECHANIC: To stop the button from moving back and forth constantly
        when the button tries to get back to its original position,
        I implemented a way to delay the button's hover movement based on if the user's
        mouse is hovering over the original position of the button.
        
        -Will optimize the code, but for now, IT WORKS!
        '''
        
        if self.done:
            if self.selected:
                if self.delay:
                    self.target_pos = self.anchor_pos
                else:
                    self.target_pos = self.hover_pos
            else:
                if self.delay and self.target_pos == self.anchor_pos:
                    self.delay = False
                self.target_pos = self.anchor_pos

        
        if pg.Vector2(self.rect.center).distance_to(pg.Vector2(self.target_pos)) > 1:
            if self.target_pos == self.hover_pos:
                self.rect.centerx += (self.target_pos[0] - self.anchor_pos[0]) / 20
                self.rect.centery += (self.target_pos[1] - self.anchor_pos[1]) / 20
                
            else:
                self.rect.centerx += (self.target_pos[0] - self.hover_pos[0]) / 20
                self.rect.centery += (self.target_pos[1] - self.hover_pos[1]) / 20
                if self.selected:
                    self.delay = True
            self.done = False
            # print((self.target_pos[1] - self.rect.centery) / 10)
            print(pg.Vector2(self.rect.center).distance_to(pg.Vector2(self.target_pos)))
        else:
            self.rect.center = self.target_pos
            self.done = True
                
    def update(self):
        mouse_pos = pg.mouse.get_pos()
        self.selected = self.rect.collidepoint(mouse_pos)
        print(self.delay)
        self.hover()
        
# Game States
class Menu(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        
        self.done = False
        self.buttons = [Button(self, pg.Vector2(300, 300))]
    
    def update(self):
        """Handle menu logic."""
        for button in self.buttons:
            button.update()
        
        
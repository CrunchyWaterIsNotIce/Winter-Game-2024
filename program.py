import pygame as pg

'''
    Where the majority of how the game logic and its components.
'''

# Game Components
class Button(pg.sprite.Sprite):
    def __init__(self, group, center_pos, img = None, cooldown = 2, distance = 20, direction = (-1, -1), speed = 10):
        super().__init__(group)
        
        #FOR DIRECTION: Upper Left -> (-1, -1), Middle = (0,0), Lower Right -> (1, 1)
        
        if img is None:
            self.image = pg.Surface([64, 64])
            self.image.fill("red")
        else:
            self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = center_pos
        
        self.anchor_pos = center_pos
        hover_direction = tuple(distance * i for i in direction)
        self.hover_pos = (hover_direction[0] + self.rect.centerx, hover_direction[1] + self.rect.centery)
        self.target_pos = self.hover_pos
        
        self.speed = speed * 10
        self.selected = False
        self.hover_done = True
        self.hover_delay = False
        
        self.time_since_clicked = 0 # In seconds
        self.cooldown = cooldown # In seconds
        self.clicked = False
        
    def click(self, dt):
        time_elapsed = pg.time.get_ticks() / 1000
        if self.selected and (time_elapsed - self.time_since_clicked > self.cooldown) and pg.mouse.get_pressed()[0]: 
            self.time_since_clicked = time_elapsed
            self.clicked = True
        else:
            self.clicked = False
        
    def hover(self, dt):
        if self.hover_done:
            if self.selected:
                if self.hover_delay:
                    self.target_pos = self.anchor_pos
                else:
                    self.target_pos = self.hover_pos
            else:
                if self.hover_delay and self.target_pos == self.anchor_pos:
                    self.hover_delay = False
                self.target_pos = self.anchor_pos
        
        distance_to_target = pg.Vector2(self.rect.center).distance_to(pg.Vector2(self.target_pos))
        if distance_to_target > 1:
            direction = pg.Vector2(self.target_pos) - pg.Vector2(self.rect.center)
            normalize_direction = direction.normalize() if distance_to_target != 0 else pg.Vector2(0,0)
            movement = normalize_direction * self.speed * dt

            self.rect.centerx += movement[0]
            self.rect.centery += movement[1]
            
            if self.target_pos == self.anchor_pos and self.selected:
                self.hover_delay = True
            self.hover_done = False
        else:
            self.rect.center = self.target_pos
            self.hover_done = True
                
    def update(self, dt):
        mouse_pos = pg.mouse.get_pos()
        self.selected = self.rect.collidepoint(mouse_pos)
        self.hover(dt)
        self.click(dt)
        
# Game States
class Menu(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        
        self.button_one = Button(self, (300, 300), direction=(0, -1), speed =20, distance=10)
        self.button_two = Button(self, (400, 300), direction=(1, 0), speed=30, distance=40)
        
        self.add(self.button_one, self.button_two)
        
    
    def update(self, dt):
        '''Handles menu logic'''
        for button in self:
            button.update(dt)
        
        if self.button_one.clicked:
            return "GAME"
        
        return None

class Game(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        
        self.button_one = Button(self, (300, 300), direction=(0, -1), speed =20, distance=10)
        
        self.add(self.button_one)
        
    def update(self, dt):
        '''Handles menu logic'''
        for button in self:
            button.update(dt)
        
        return None
        
        
import pygame as pg
import os, math

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
        
        self.time_since_clicked = 0
        self.cooldown = cooldown
        self.clicked = False
        
    def click(self, dt):
        time_elapsed = pg.time.get_ticks() / 1000
        if self.selected and ((time_elapsed - self.time_since_clicked > self.cooldown) or self.time_since_clicked == 0) and pg.mouse.get_pressed()[0]: 
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
    
class Player(pg.sprite.Sprite):
    def __init__(self, group, center_pos, img = None):
        super().__init__(group)
        if img is None:
            self.image = pg.Surface([64, 64])
            self.image.fill("red")
        else:
            self.image = img

        self.rect = self.image.get_rect()
        self.rect.center = center_pos
        self.direction = pg.math.Vector2()
        
        self.moving = False
        self.steps = 0
    def controls(self, dt):
        keys = pg.key.get_pressed()

        self.moving = keys[pg.K_w] or keys[pg.K_a] or keys[pg.K_s] or keys[pg.K_d]
        
        if keys[pg.K_w]:
            self.direction.y = -1
        elif keys[pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pg.K_a]:
            self.direction.x = -1
        elif keys[pg.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if self.moving and self.direction != pg.Vector2(0, 0):
            if self.steps < math.pi / 2: # Seperate statement to avoid 1.1
                self.steps = round(self.steps + 0.05, 2) 
        elif self.steps > 0:
            self.steps = round(self.steps - 0.05, 2)
        
        self.rect.center += self.direction * 100 * dt * math.sin(self.steps)
        

    def update(self, dt):
        self.controls(dt)
        print(self.moving, self.steps)
        
        
# Game States
class Menu(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        
        self.play = Button(self, (385, 400), img=pg.transform.scale_by(pg.image.load(os.path.join("assets", "play_button.png")), 3), direction=(0, -1))
        self.info = Button(self, (185, 400), img=pg.transform.scale_by(pg.image.load(os.path.join("assets", "info_button.png")), 3), direction=(0, -1))
        self.option = Button(self, (585, 400), img=pg.transform.scale_by(pg.image.load(os.path.join("assets", "option_button.png")), 3), direction=(0, -1))
    
    def update(self, dt):
        '''Handles menu logic'''
        for button in self:
            button.update(dt)
        
        if self.play.clicked:
            return "GAME"
        
        return None

class Game(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        
        self.player = Player(self, (385, 385), pg.transform.scale_by(pg.image.load(os.path.join("assets", "player.png")), 3))
        
            
        
    def update(self, dt):
        self.player.update(dt)
        
        return None
        
        
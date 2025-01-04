import pygame as pg

'''
    Where the majority of how the application logic and its components.
'''

class Control:
    def __init__(self, caption, size):
        pg.init()

        ''' Required Properties of Application '''
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(caption)
        self.clock = pg.time.Clock()
        self.running = True
        
        ''' Required Properties of Game '''
        self.state_machine = None
        
    
    def initialize_state_machine(self, states):
        self.state_machine = State_Machine(states)
        self.state_machine.set_state("MENU")

    def event_handler(self):
        ''' Global Events '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def run(self):
        ''' Main Program Loop '''
        while self.running:
            dt = self.clock.tick(60) / 1000 # In Seconds
            self.event_handler()
            
            self.state_machine.update(dt)
            
            self.screen.fill("light blue")
            self.state_machine.draw(self.screen)
            
            pg.display.flip()
            
        pg.quit()
    
class State_Machine:
    def __init__(self, states):
        self.states = states
        self.current_state = None
    
    def set_state(self, state):
        try:
            self.current_state = self.states[state]
        except ValueError:
            print("State is invalid")
    
    def update(self, dt):
        if self.current_state:
            self.current_state.update(dt)
    
    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)
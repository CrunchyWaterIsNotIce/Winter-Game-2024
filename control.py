import pygame as pg



'''
    Where the majority of how the program functions and its components.
'''

class Control:
    def __init__(self, caption, size):
        pg.init()

        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(caption)
        self.clock = pg.time.Clock()
        
        self.running = True
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
            # print(self.clock.get_fps())
            self.event_handler()
            self.state_machine.update()
            
            self.state_machine.draw(self.screen)
            
            self.clock.tick(60)
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
        
        print(self.current_state)
    
    def update(self):
        if self.current_state:
            self.current_state.update()
    
    def draw(self, screen):
        if self.current_state:
            self.current_state.draw(screen)
        


        
        
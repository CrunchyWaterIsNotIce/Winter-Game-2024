import pygame

pygame.init()

window = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill("black")
    
    
    pygame.display.flip()
    

if __name__ == "__main__":
    print('bruh')
        


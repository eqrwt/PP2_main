import pygame
pygame.init()

W = 600
H = 600

clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))

pygame.display.set_caption("Ball")

def drawcircle(a = 0, b = 0):
    pygame.draw.circle(screen, (0, 255, 255), (a, b), 25)

x = 60
y = 68

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
    screen.fill((0, 0, 0))
   
    drawcircle(x, y)
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and y > 30:  y -= 20
    if key[pygame.K_DOWN] and y < 575:  y += 20
    if key[pygame.K_LEFT] and x > 30:  x -= 20
    if key[pygame.K_RIGHT] and x < 575:  x += 20
    
    pygame.display.update()
    clock.tick(120)
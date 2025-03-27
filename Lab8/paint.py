import pygame

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Default settings
radius = 15
mode = 'blue'
points = []
drawing_shape = None 
start_pos = None  
eraser_mode = False  

# Colors dictionary
colors = {
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'white': (255, 255, 255),
    'purple': (128, 0, 128),
    'black': (0, 0, 0)  # Background color for eraser
}

def drawLineBetween(screen, start, end, width, color):
    pygame.draw.line(screen, color, start, end, width)

def main():
    # Default settings
    radius = 15
    mode = 'blue'
    points = []
    drawing_shape = None 
    start_pos = None  
    eraser_mode = False  
    running = True

    # Keep a copy of the screen to restore erased areas
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))

    while running:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    running = False
                if event.key == pygame.K_F4 and alt_held:
                    running = False
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                # Color selection
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'
                elif event.key == pygame.K_w:
                    mode = 'white'
                elif event.key == pygame.K_p:
                    mode = 'purple'
                
                # Shape selection
                elif event.key == pygame.K_LSHIFT:
                    drawing_shape = "rectangle"
                elif event.key == pygame.K_c:
                    drawing_shape = "circle"
                elif event.key == pygame.K_e:
                    eraser_mode = not eraser_mode  # Toggle eraser mode

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LSHIFT, pygame.K_c]:
                    drawing_shape = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    start_pos = event.pos  # Capture start position for shapes
                    if not drawing_shape:
                        points.append(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing_shape and start_pos:
                    end_pos = event.pos
                    if drawing_shape == "rectangle":
                        pygame.draw.rect(background, colors[mode], pygame.Rect(*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
                    elif drawing_shape == "circle":
                        center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                        radius = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                        pygame.draw.circle(background, colors[mode], center, radius, 2)
                    start_pos = None  # Reset

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if not drawing_shape:
                    if eraser_mode:
                        pygame.draw.circle(background, (0, 0, 0), position, radius * 2)  # Restore background
                    else:
                        points.append(position)
                        points = points[-256:]

        # Refresh screen
        screen.blit(background, (0, 0))
        
        # Draw lines
        for i in range(len(points) - 1):
            drawLineBetween(screen, points[i], points[i + 1], radius, colors[mode])

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

main()

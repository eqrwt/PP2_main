import pygame

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Default settings
radius = 15
mode = 'blue'
points = []  # Initialize points as an empty list
drawing_shape = None 
start_pos = None  
eraser_mode = False  
pencil_mode = False  # New: Pencil mode

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

def display_mode_info(screen, mode, drawing_shape, eraser_mode, pencil_mode):
    font = pygame.font.SysFont('Arial', 24)
    text = f"Mode: {mode.capitalize()}"
    if eraser_mode:
        text = f"Eraser Mode"
    elif pencil_mode:
        text = f"Pencil Mode"
    elif drawing_shape:
        text = f"Drawing: {drawing_shape.capitalize()}"

    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

def main():
    global mode, drawing_shape, start_pos, eraser_mode, pencil_mode, radius, points
    running = True

    # Keep a copy of the screen to restore erased areas
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
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
                elif event.key == pygame.K_t:
                    drawing_shape = "equilateral_triangle"
                elif event.key == pygame.K_y:
                    drawing_shape = "right_triangle"
                elif event.key == pygame.K_c:
                    drawing_shape = "circle"
                elif event.key == pygame.K_s:
                    drawing_shape = "square"
                elif event.key == pygame.K_h:
                    drawing_shape = "rhombus"
                elif event.key == pygame.K_LSHIFT:
                    drawing_shape = "rectangle"
                elif event.key == pygame.K_e:
                    eraser_mode = not eraser_mode  # Toggle eraser mode
                elif event.key == pygame.K_l:
                    pencil_mode = not pencil_mode  # Toggle pencil mode
                    if not pencil_mode:
                        points = []  # Clear points when pencil mode is turned off

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LSHIFT, pygame.K_c, pygame.K_t, pygame.K_y, pygame.K_s, pygame.K_h]:
                    drawing_shape = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    start_pos = event.pos  # Capture start position for shapes
                    if pencil_mode:
                        points.append(event.pos)  # Add points when pencil mode is on

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing_shape and start_pos:
                    end_pos = event.pos
                    if drawing_shape == "rectangle":
                        pygame.draw.rect(background, colors[mode], pygame.Rect(*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
                    elif drawing_shape == "circle":
                        center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                        radius = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                        pygame.draw.circle(background, colors[mode], center, radius, 2)
                    elif drawing_shape == "equilateral_triangle":
                        pygame.draw.polygon(background, colors[mode], [start_pos, (start_pos[0] + 50, start_pos[1] + 50), (start_pos[0] - 50, start_pos[1] + 50)], 2)
                    elif drawing_shape == "right_triangle":
                        pygame.draw.polygon(background, colors[mode], [start_pos, (start_pos[0] + 50, start_pos[1]), (start_pos[0], start_pos[1] + 50)], 2)
                    elif drawing_shape == "square":
                        side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                        pygame.draw.rect(background, colors[mode], pygame.Rect(start_pos[0], start_pos[1], side, side), 2)
                    elif drawing_shape == "rhombus":
                        pygame.draw.polygon(background, colors[mode], [start_pos, (start_pos[0] + 50, start_pos[1] + 50), (start_pos[0], start_pos[1] + 100), (start_pos[0] - 50, start_pos[1] + 50)], 2)
                    start_pos = None  # Reset

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if pencil_mode:
                    points.append(position)  # Add points while moving the mouse in pencil mode
                    points = points[-256:]  # Limit points to the last 256 to avoid memory issues
                elif eraser_mode:
                    if radius:  # Make sure radius is defined before using it
                        pygame.draw.circle(background, (0, 0, 0), position, radius * 2)  # Restore background

        # Refresh screen
        screen.blit(background, (0, 0))

        # Draw pencil lines
        if pencil_mode:
            for i in range(len(points) - 1):
                pygame.draw.line(screen, colors[mode], points[i], points[i + 1], radius)

        # Display the current mode on the top left
        display_mode_info(screen, mode, drawing_shape, eraser_mode, pencil_mode)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

main()

import pygame
import random

pygame.init()

# Screen size
width = 600
height = 400

# Game screen setup
screen = pygame.display.set_mode((width, height))

# Variables initialization
score = 0
level = 1
speed = 200
fruit_eaten = False
next_level_score = 30
last_score = 0
food_lifetime = 8000 # 5 seconds for dissapearing food
food_timer = 0

# Snake starting position
head_square = [100, 100]
squares = [[x, 100] for x in range(30, 90, 10)]  # Initial snake body

# Function to generate a valid food position
def generate_food():
    while True:
        fr_x = random.randrange(0, width // 10) * 10
        fr_y = random.randrange(0, height // 10) * 10
        fruit_coor = [fr_x, fr_y]
        
        # Ensure the food does not spawn on the snake
        if fruit_coor not in squares:
            return fruit_coor

# Generate initial fruit position
fruit_coor = generate_food()
food_timer = pygame.time.get_ticks()

# Directions
direction = "right"
next_dir = "right"

done = False

def game_over():
    """Ends the game and shows final score."""
    global done
    g_o_font = pygame.font.SysFont("times new roman", 30)
    g_o_surface = g_o_font.render(f"Game Over, your score: {score} and level: {level}", True, (255, 0, 0))
    g_o_rect = g_o_surface.get_rect(center=(width//2, height//2))

    screen.fill((0, 0, 0))
    screen.blit(g_o_surface, g_o_rect)
    pygame.display.update()

    pygame.time.delay(4000)
    pygame.quit()
    exit()

# Main game loop
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and direction != "up":
                next_dir = "down"
            if event.key == pygame.K_UP and direction != "down":
                next_dir = "up"
            if event.key == pygame.K_LEFT and direction != "right":
                next_dir = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                next_dir = "right"
    
    # Update direction if valid
    direction = next_dir

    # Move the snake
    if direction == "right":
        head_square[0] += 10
    if direction == "left":
        head_square[0] -= 10
    if direction == "up":
        head_square[1] -= 10
    if direction == "down":
        head_square[1] += 10

    # Check for wall collision
    if head_square[0] < 0 or head_square[0] >= width or head_square[1] < 0 or head_square[1] >= height:
        game_over()

    # Check for self-collision AFTER moving
    for square in squares[:-1]:
        if head_square[0] == square[0] and head_square[1] == square[1]:
            game_over()

    # Add new head position
    new_square = head_square.copy()
    squares.append(new_square)

    # Check if food is eaten
    if head_square == fruit_coor:
        fruit_eaten = True
        fruit_weight = random.choice([10, 20, 30])
        score += fruit_weight
        fruit_coor = generate_food()  # Generate new food
        food_timer = pygame.time.get_ticks()

    else:
        squares.pop(0)  # Remove tail if food is not eaten
    
    if fruit_eaten:
        fruit_coor = generate_food()
        fruit_eaten = False

        # Increase level every 30 points
        if score >= last_score + next_level_score:
            level += 1
            speed = max(50, speed - 20) 
            last_score = score

    if pygame.time.get_ticks() - food_timer > food_lifetime:
        food_timer = pygame.time.get_ticks()
        fruit_coor = generate_food()
    
    # Drawing section
    screen.fill((0, 0, 0))  # Clear the screen

    # Draw snake
    for square in squares:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(square[0], square[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit_coor[0], fruit_coor[1], 10, 10))

    # Display score
    font = pygame.font.SysFont("times new roman", 20)
    score_surface = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

    pygame.display.flip()
    pygame.time.delay(speed)  # Adjust speed based on level

pygame.quit()

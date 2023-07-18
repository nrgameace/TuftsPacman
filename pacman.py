import pygame, os, time, random

pygame.display.set_caption('Pacman')
icon_image = pygame.image.load('PacmanImage.png')
pygame.display.set_icon(icon_image)
#Sets Up Game
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 3, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 3, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 3, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 3, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]





BLACK = (0, 0, 0)
BLUE = (0, 0, 175)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
DARK_BLUE = (3,37,126)





#Set Up Game
pygame.init()
font_name = pygame.font.get_default_font()
GAME_W,GAME_H = 960, 960
SCREEN_WIDTH,SCREEN_HEIGHT = 800, 800
game_canvas = pygame.Surface((GAME_W,GAME_H))
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
running, playing = True, True
dt, prev_time = 0, 0
open_tiles = [[]]
FPS = 30
clock = pygame.time.Clock()

#Set Up Pacman
pacman_radius = 12
pacman_position = [(GAME_W)/2, (GAME_H) - 240]
pacman_direction = [0, 0]
pacman_speed = 2
score = 0
power_up_active = False
power_up_duration = 10
power_up_timer = 0
collisions = False
pacman_lives = 3


# Set up ghosts
num_ghosts = 4
ghost_height, ghost_width = 28, 28
ghost_positions = []
ghost_directions = []
ghost_speed = 1.5
ghost_colors = [LIGHT_BLUE, RED, PINK, ORANGE]
ghosts = []
ghosts_eliminated = []
for i in range(num_ghosts):
    ghost_positions.append([(GAME_W)/2, (GAME_H)/2])
    number = round(random.randint(0,3))
    if number == 0:
        ghost_directions.append([0,1])
    elif number == 1:
        ghost_directions.append([1,0])
    elif number == 2:
        ghost_directions.append([0,-1])
    elif number == 3:
        ghost_directions.append([-1,0])
    

#Set Up Tiles
current_tile = []
top_tile = []
bottom_tile = []
left_tile = []
right_tile = []

# Function to move pacman from one side to the other.
def teleport():
    if pacman_position[0] <= 0:
        pacman_position[0] = 920
        return True
    elif pacman_position[0] >= 945:
        pacman_position[0] = 20
        return True
    return False

# Helper function to check collisions
def check_collision(x, y):
    map_x = int(x / 32)
    map_y = int(y / 32)
    if map_data[map_y][map_x] == 1:  # Wall
        return True
    return False

# Draw Text Function for Scoreboard
def draw_text(text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    game_canvas.blit(text_surface, text_rect.center)
    

# Function for drawing the map
def draw_map():
    for row in range(len(map_data)):
        for col in range(len(map_data[row])):
            tile = map_data[row][col]
            x = col * 32  # Adjust the tile size as needed
            y = row * 32
            if tile == 1:
                pygame.draw.rect(game_canvas, BLUE, (x, y, 32, 32))
            elif tile == 0:
                pygame.draw.circle(game_canvas, WHITE, [x+16, y+16], 3)
                open_tiles.append([row, col])
            elif tile == 2:
                pygame.draw.rect(game_canvas, BLACK, (x, y, 32, 32))
                open_tiles.append([row, col])
            elif tile == 3:
                pygame.draw.circle(game_canvas, YELLOW, [x+16, y+16], 7)
                open_tiles.append([row, col])

            

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Change Pac-Man direction
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pacman_direction = [-1, 0]
        elif event.key == pygame.K_RIGHT:
            pacman_direction = [1, 0]
        elif event.key == pygame.K_UP:
            pacman_direction = [0, -1]
        elif event.key == pygame.K_DOWN:
            pacman_direction = [0, 1]
    
    pacman_position[0] += pacman_direction[0] * pacman_speed
    pacman_position[1] += pacman_direction[1] * pacman_speed
    pacman_x = int(pacman_position[0]/32)
    pacman_y = int(pacman_position[1]/32)
    
    # #Ghost change direction
    # for i in range(num_ghosts):
    #     if check_collision()

    

    # Check for Pacman border collisions
    if pacman_position[0] < 0:
        pacman_position[0] = GAME_W - pacman_radius
    elif pacman_position[0] >= GAME_W:
        pacman_position[0] = 0
    elif pacman_position[1] < 0:
        pacman_position[1] = GAME_H - pacman_radius
    elif pacman_position[1] >= GAME_H:
        pacman_position[1] = 0
    
    # Check for Ghost border collisions
    for i in range(num_ghosts):
        if ghost_positions[i][0] < 0:
            ghost_positions[i][0] = GAME_W - (ghost_width/2)
        elif ghost_positions[i][0] >= GAME_W:
            ghost_positions[i][0] = 0
        elif ghost_positions[i][1] < 0:
            ghost_positions[i][1] = GAME_H - (ghost_height/2)
        elif ghost_positions[i][1] >= GAME_H:
            ghost_positions[i][1] = 0

    #Teleport
    teleport()
    
    #Check for Pacman wall collisions
    if not teleport():
        if check_collision(pacman_position[0] - pacman_radius, pacman_position[1] - pacman_radius):
            pacman_position[0] -= pacman_direction[0] * pacman_speed
            pacman_position[1] -= pacman_direction[1] * pacman_speed
        if check_collision(pacman_position[0] + pacman_radius, pacman_position[1] + pacman_radius):
            pacman_position[0] -= pacman_direction[0] * pacman_speed
            pacman_position[1] -= pacman_direction[1] * pacman_speed
        if check_collision(pacman_position[0] - pacman_radius, pacman_position[1] + pacman_radius):
            pacman_position[0] -= pacman_direction[0] * pacman_speed
            pacman_position[1] -= pacman_direction[1] * pacman_speed
        if check_collision(pacman_position[0] + pacman_radius, pacman_position[1] - pacman_radius):
            pacman_position[0] -= pacman_direction[0] * pacman_speed
            pacman_position[1] -= pacman_direction[1] * pacman_speed
    
    # Check for Ghosts wall collisions
    for i in range(num_ghosts):
        if not teleport():
            if check_collision(ghost_positions[i][0] - (ghost_width), ghost_positions[i][1] - (ghost_height)):
                ghost_positions[i][0] -= ghost_directions[i][0] * ghost_speed
                ghost_positions[i][1] -= ghost_directions[i][1] * ghost_speed
                # ghost_directions[i].clear()
                # number = round(random.randint(0,3))
                # if number == 0:
                #     ghost_directions.append([0,1])
                # elif number == 1:
                #     ghost_directions.append([1,0])
                # elif number == 2:
                #     ghost_directions.append([0,-1])
                # elif number == 3:
                #     ghost_directions.append([-1,0])
            if check_collision(ghost_positions[i][0] + (ghost_width), ghost_positions[i][1] + (ghost_height)):
                ghost_positions[i][0] -= ghost_directions[i][0] * ghost_speed
                ghost_positions[i][1] -= ghost_directions[i][1] * ghost_speed
            if check_collision(ghost_positions[i][0] - (ghost_width), ghost_positions[i][1] + (ghost_height)):
                ghost_positions[0] -= ghost_directions[0] * ghost_speed
                ghost_positions[1] -= ghost_directions[1] * ghost_speed
            if check_collision(ghost_positions[i][0] + (ghost_width), ghost_positions[i][1] - (ghost_height)):
                ghost_positions[0] -= ghost_directions[0] * ghost_speed
                ghost_positions[1] -= ghost_directions[1] * ghost_speed
    
    # Check for dot collisions
    map_x = int(pacman_position[0] / 32)
    map_y = int(pacman_position[1] / 32)
    if map_data[map_y][map_x] == 0:  # Dot
        map_data[map_y][map_x] = 2
        score += 10
        
    
    # Check for power-up collisions
    elif map_data[map_y][map_x] == 3:  # Power-up
        map_data[map_y][map_x] = 2
        score += 50
        power_up_active = True
        power_up_timer = power_up_duration
        

    #Checks whether or not pacman has an active powerup, the outcome of pacman's collision with a ghost depends on if the power up is active or not.    
    if power_up_active:
        ghost_colors = [DARK_BLUE, DARK_BLUE, DARK_BLUE, DARK_BLUE]
        power_up_timer -= 1/60
        collisions = True
        if power_up_timer <= 0:
            power_up_active = False
            collisions = False
            ghost_colors = [LIGHT_BLUE, RED, PINK, ORANGE]
            
    
    



    # Move ghosts
    for i in range(num_ghosts):
        ghost_positions[i][0] += ghost_directions[i][0] * ghost_speed 
        ghost_positions[i][1] += ghost_directions[i][1] * ghost_speed

    if collisions == True:
        for i in range(num_ghosts):
            if pacman_x == int(ghost_positions[i][0]/32) and pacman_y == int(ghost_positions[i][1]/32):
                ghost_positions[i][0] = GAME_W/2
                ghost_positions[i][1] = GAME_H/2
                score += 200
    elif collisions == False:
        for i in range(num_ghosts):
            if pacman_x == int(ghost_positions[i][0]/32) and pacman_y == int(ghost_positions[i][1]/32):
                pacman_position = [(GAME_W)/2, (GAME_H) - 240]
                ghost_positions[i][0] = GAME_W/2
                ghost_positions[i][1] = GAME_H/2
                pacman_lives -= 1
    
    
    #Clear the screen
    game_canvas.fill(BLACK)

    # Draw Map
    draw_map()
    #Draw Ghosts
    for i in range(num_ghosts):
        pygame.draw.rect(game_canvas, ghost_colors[i], (ghost_positions[i][0], ghost_positions[i][1], ghost_width, ghost_height))
    # Draw Pac-Man
    pygame.draw.circle(game_canvas, YELLOW, pacman_position, pacman_radius)
    
    

    #Rescale screen to fit game window
    draw_text(f"Score: " + str(score) + "     " + str(pacman_lives), 25, 455, 10)

    screen.blit(pygame.transform.scale(game_canvas,(SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))
    #Update the display
    
    if pacman_lives > 0:
        pygame.display.flip()
    else:
        game_canvas.fill(BLACK)
        draw_text("GAME OVER", 50, GAME_W/2, GAME_H/2)
        screen.blit(pygame.transform.scale(game_canvas,(SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()


# Limit the frame rate
    clock.tick(60)

# Quit the game


pygame.quit()
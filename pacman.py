import pygame, os, time, random

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





#Set Up Game
pygame.init()
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
pacman_radius = 14
pacman_position = [(GAME_W)/2, (GAME_H) - 240]
pacman_direction = [0, 0]
pacman_speed = 2


# Set up ghosts
num_ghosts = 4
ghost_height, ghost_width = 32, 32
ghost_positions = []
ghost_directions = []
ghost_speed = 1.5
ghost_colors = [LIGHT_BLUE, RED, PINK, ORANGE]
ghosts = []
for i in range(num_ghosts):
    ghost_positions.append([(GAME_W)/2, (GAME_H)/2])
    number = round(random.randint(0,1))
    if number == 0:
        ghost_directions.append([0,1])
    elif number == 1:
        ghost_directions.append([1,0])

#Set Up Tiles
current_tile = []
top_tile = []
bottom_tile = []
left_tile = []
right_tile = []

# def check_tile_pacman():
#     current_tile.clear()
#     top_tile.clear()
#     bottom_tile.clear()
#     left_tile.clear()
#     right_tile.clear()

#     current_tile.append(map_data[round(pacman_position[1] / 32)][round(pacman_position[0] / 32)])
#     top_tile.append(map_data[round((pacman_position[1] - 32) / 32)][round(pacman_position[0] / 32)])
#     bottom_tile.append(map_data[round((pacman_position[1] + 32) / 32)][round(pacman_position[0] / 32)])
#     left_tile.append(map_data[round(pacman_position[1] / 32)][round((pacman_position[0] - 32) / 32)])
#     right_tile.append(map_data[round(pacman_position[1] / 32)][round((pacman_position[0] + 32) / 32)])



     
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

    # Check for border collisions
    if pacman_position[0] < 0:
        pacman_position[0] = GAME_W - pacman_radius
    elif pacman_position[0] >= GAME_W:
        pacman_position[0] = 0
    elif pacman_position[1] < 0:
        pacman_position[1] = GAME_H - pacman_radius
    elif pacman_position[1] >= GAME_H:
        pacman_position[1] = 0
    
    #Teleport
    teleport()

    # Check for wall collisions
    if not teleport():
        if check_collision(pacman_position[0] - pacman_radius, pacman_position[1] - pacman_radius):
            pacman_position[0] -= pacman_direction[0] * pacman_speed
            pacman_position[1] -= pacman_direction[1] * pacman_speed
        if check_collision(pacman_position[0] + pacman_radius, pacman_position[1] + pacman_radius):
            pacman_position[0] -= pacman_direction[0] * pacman_speed
            pacman_position[1] -= pacman_direction[1] * pacman_speed
    
    # Check for dot collisions
    map_x = int(pacman_position[0] / 32)
    map_y = int(pacman_position[1] / 32)
    if map_data[map_y][map_x] == 0:  # Dot
        map_data[map_y][map_x] = 2

    # Check for power-up collisions
    elif map_data[map_y][map_x] == 3:  # Power-up
        map_data[map_y][map_x] = 2





    # Move ghosts
    for i in range(num_ghosts):
        ghost_positions[i][0] += ghost_directions[i][0] * ghost_speed 
        ghost_positions[i][1] += ghost_directions[i][1] * ghost_speed
    
    #Clear the screen
    game_canvas.fill(BLACK)

    # Draw Map
    draw_map()
    # Draw Pac-Man
    pacman_x = pacman_position[0] - pacman_radius if pacman_direction[0] < 0 else pacman_position[0]
    pacman_y = pacman_position[1] - pacman_radius if pacman_direction[1] < 0 else pacman_position[1]
    pygame.draw.circle(game_canvas, YELLOW, pacman_position, pacman_radius)
    #Draw ghosts
    for i in range(num_ghosts):
        pygame.draw.circle(game_canvas, ghost_colors[i], ghost_positions[i], ghost_height)

    #Rescale screen to fit game window
    screen.blit(pygame.transform.scale(game_canvas,(SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))
    #Update the display
    pygame.display.flip()

# Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
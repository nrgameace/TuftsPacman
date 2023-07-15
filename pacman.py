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

current_tile = []
top_tile = []
bottom_tile = []
left_tile = []
right_tile = []



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
pacman_radius = 16
pacman_position = [(GAME_W)/2, (GAME_H) - 240]
pacman_direction = [0, 0]
pacman_speed = 5


# Set up ghosts
num_ghosts = 4
ghost_height, ghost_width = 32, 32
ghost_positions = []
ghost_directions = []
ghost_speed = 3
ghost_colors = [LIGHT_BLUE, RED, PINK, ORANGE]
ghosts = []
for i in range(num_ghosts):
    ghost_positions.append([(GAME_W)/2, (GAME_H)/2])
    number = round(random.randint(0,1))
    if number == 0:
        ghost_directions.append([0,1])
    elif number == 1:
        ghost_directions.append([1,0])

def check_tile():
    current_tile = map_data[round(pacman_position[0]/32), round(pacman_position[1]/32)]
    top_tile = map_data[round(pacman_position[0]/32), round(pacman_position[1]/32)-1]
    bottom_tile = map_data[round(pacman_position[0]/32), round(pacman_position[1]/32)+1]
    left_tile = map_data[round(pacman_position[0]/32)-1, round(pacman_position[1]/32)]
    right_tile = map_data[round(pacman_position[0]/32)+1, round(pacman_position[1]/32)]

    

    
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
            pacman_direction = [-0.5, 0]
        elif event.key == pygame.K_RIGHT:
            pacman_direction = [0.5, 0]
        elif event.key == pygame.K_UP:
            pacman_direction = [0, -0.5]
        elif event.key == pygame.K_DOWN:
            pacman_direction = [0, 0.5]


    # Move Pac-Man
    pacman_position[0] += pacman_direction[0] * pacman_speed
    pacman_position[1] += pacman_direction[1] * pacman_speed

    # Move ghosts
    for i in range(num_ghosts):
        ghost_positions[i][0] += ghost_directions[i][0] * ghost_speed 
        ghost_positions[i][1] += ghost_directions[i][1] * ghost_speed
    
    #Clear the screen
    game_canvas.fill(BLACK)

    # Draw Map
    draw_map()
    # Draw Pac-Man
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
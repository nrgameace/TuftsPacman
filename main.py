import pygame, random

pygame.display.set_caption('Pacman')
icon_image = pygame.image.load('PacmanImage.png')
pygame.display.set_icon(icon_image)
#Sets up game and grid system
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
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2],
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
pellets = 294




#Sets up basic colors with RGB numbers
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
DARK_BLUE = (3,37,126)



#Set up game, display dimensions and framerate
pygame.init()
font_name = pygame.font.get_default_font()
GAME_W,GAME_H = 960, 960
SCREEN_WIDTH,SCREEN_HEIGHT = 800, 800
game_canvas = pygame.Surface((GAME_W,GAME_H))
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
running, playing = True, True
dt, prev_time = 0, 0
open_tiles = [[]]
FPS = 60
clock = pygame.time.Clock()

#Loads the the png files as sprites
pacman_half_img = pygame.transform.scale(pygame.image.load('./pacmansprites/pacman_half.png'), (32, 32))
pacman_half_up_img = pygame.transform.scale(pygame.image.load('./pacmansprites/pacman_half_up.png'), (32,32))
pacman_half_down_img = pygame.transform.scale(pygame.image.load('./pacmansprites/pacman_half_down.png'), (32, 32))
pacman_half_left_img = pygame.transform.scale(pygame.image.load('./pacmansprites/pacman_half_left.png'), (32, 32))
pacman_open_img = pygame.transform.scale(pygame.image.load('./pacmansprites/pacman_open.png'), (32,32))
pacman_open_up_img = pygame.transform.scale(pygame.image.load('./pacmansprites/pacman_open_up.png'), (32, 32))
pacman_open_down_img = pygame.transform.scale(pygame.image.load('./pacmansprites/pacman_open_down.png'), (32, 32))
pacman_open_left_img = pygame.transform.scale(pygame.image.load('./pacmansprites/pacman_open_left.png'), (32, 32))
ghost_1_img = pygame.transform.scale(pygame.image.load('./pacmansprites/ghost_1.png'), (32, 32))
orange_1_img = pygame.transform.scale(pygame.image.load('./pacmansprites/orange_1.png'), (32,32))
pinky_1_img = pygame.transform.scale(pygame.image.load('./pacmansprites/pinky_1.png'), (32,32))
red_1_img = pygame.transform.scale(pygame.image.load('./pacmansprites/red_1.png'), (32,32))
blue_1_img = pygame.transform.scale(pygame.image.load('./pacmansprites/blue_1.png'), (32,32))
pacman_dir_img = pacman_half_img




#Set Up Pacman
pacman_radius = 10
pacman_position = [(GAME_W)/2, (GAME_H) - 240]
pacman_direction = [0, 0]
pacman_speed = 2
score = 0
power_up_active = False
power_up_duration = 10
power_up_timer = 0
collisions = False
pacman_lives = 3
mouth_open = True
r = 1
l = 0
u = 0
d = 0


# Set up ghosts
num_ghosts = 4
ghost_height, ghost_width = 25, 25
ghost_positions = []
ghost_directions = []
ghost_speed = 3
ghost_colors = [blue_1_img, red_1_img, pinky_1_img, orange_1_img]
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
    if pacman_position[0] <= 10:
        pacman_position[0] = 940
        return True
    elif pacman_position[0] >= 950:
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

# Function that opens and closes Pac-Man's mouth
def toggle_mouth():
    global mouth_open
    mouth_open = not mouth_open
last_toggle_time = pygame.time.get_ticks()

            
# The start of the game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
    #Toggles Pac-Man's mouth every time it renders
    if pygame.time.get_ticks() - last_toggle_time >= 250:
        toggle_mouth()
        last_toggle_time = pygame.time.get_ticks()


    # Change Pac-Man direction
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pacman_direction = [-1, 0]
            l = 1
            r = 0
            u = 0
            d = 0
        elif event.key == pygame.K_RIGHT:
            pacman_direction = [1, 0]
            r = 1
            l = 0
            u = 0
            d = 0
        elif event.key == pygame.K_UP:
            pacman_direction = [0, -1]
            u = 1
            r = 0
            l = 0
            d = 0
        elif event.key == pygame.K_DOWN:
            pacman_direction = [0, 1]
            d = 1
            u = 0
            r = 0
            l = 0
    
    pacman_position[0] += pacman_direction[0] * pacman_speed
    pacman_position[1] += pacman_direction[1] * pacman_speed
    pacman_x = int(pacman_position[0]/32)
    pacman_y = int(pacman_position[1]/32)

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
            if check_collision(ghost_positions[i][0], ghost_positions[i][1]):
                ghost_positions[i][0] -= ghost_directions[i][0] * ghost_speed
                ghost_positions[i][1] -= ghost_directions[i][1] * ghost_speed
                number = round(random.randint(0,2))
                if number == 0:
                    ghost_directions[i] = [0,1]
                elif number == 1:
                    ghost_directions[i] = [1,0]
                elif number == 2:
                    ghost_directions[i] = [-1,0]
                
            if check_collision(ghost_positions[i][0] + (ghost_width), ghost_positions[i][1] + (ghost_height)):
                ghost_positions[i][0] -= ghost_directions[i][0] * ghost_speed
                ghost_positions[i][1] -= ghost_directions[i][1] * ghost_speed
                
                number = round(random.randint(0,2))
                if number == 0:
                    ghost_directions[i] = [0,-1]
                elif number == 1:
                    ghost_directions[i] = [1,0]
                elif number == 2:
                    ghost_directions[i] = [-1,0]
            if check_collision(ghost_positions[i][0], ghost_positions[i][1] + (ghost_height)):
                ghost_positions[i][0] -= ghost_directions[i][0] * ghost_speed
                ghost_positions[i][1] -= ghost_directions[i][1] * ghost_speed
                
                number = round(random.randint(0,2))
                if number == 0:
                    ghost_directions[i] = [0,1]
                elif number == 1:
                    ghost_directions[i] = [1,0]
                elif number == 2:
                    ghost_directions[i] = [0,-1]
            if check_collision(ghost_positions[i][0] + (ghost_width), ghost_positions[i][1]):
                ghost_positions[i][0] -= ghost_directions[i][0] * ghost_speed
                ghost_positions[i][1] -= ghost_directions[i][1] * ghost_speed
                number = round(random.randint(0,2))
                if number == 0:
                    ghost_directions[i] = [0,1]
                elif number == 1:
                    ghost_directions[i] = [0,-1]
                elif number == 2:
                    ghost_directions[i] = [-1,0]
    
    # Check for dot collisions
    map_x = int(pacman_position[0] / 32)
    map_y = int(pacman_position[1] / 32)
    if map_data[map_y][map_x] == 0:  # Dot
        map_data[map_y][map_x] = 2
        score += 10
        pellets -= 1
        
    
    # Check for power-up collisions
    elif map_data[map_y][map_x] == 3:  # Power-up
        map_data[map_y][map_x] = 2
        score += 50
        power_up_active = True
        power_up_timer = power_up_duration
        

    #Checks whether or not pacman has an active powerup, the outcome of pacman's collision with a ghost depends on if the power up is active or not.    
    if power_up_active:
        ghost_colors = [ghost_1_img, ghost_1_img, ghost_1_img, ghost_1_img]
        power_up_timer -= 1/60
        collisions = True
        if power_up_timer <= 0:
            power_up_active = False
            collisions = False
            ghost_colors = [blue_1_img, red_1_img, pinky_1_img, orange_1_img]
            
    
    



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
    
    # Animates Pac-Man so when he moves up or down his face follows the direction   
    if mouth_open:
        pacman_right_img = pacman_open_img
        pacman_left_img = pacman_open_left_img
        pacman_up_img = pacman_open_up_img
        pacman_down_img = pacman_open_down_img
    elif not mouth_open:
        pacman_right_img = pacman_half_img
        pacman_left_img = pacman_half_left_img
        pacman_up_img = pacman_half_up_img
        pacman_down_img = pacman_half_down_img

    
    

    

    if r == 1:
        pacman_dir_img = pacman_right_img
    elif l == 1:
        pacman_dir_img = pacman_left_img
    elif u == 1:
        pacman_dir_img = pacman_up_img
    elif d == 1:
        pacman_dir_img = pacman_down_img
    #Draw Ghosts
    for i in range(num_ghosts):
        #pygame.draw.rect(game_canvas, ghost_colors[i], (ghost_positions[i][0], ghost_positions[i][1], ghost_width, ghost_height))
        game_canvas.blit(ghost_colors[i], (ghost_positions[i][0] , ghost_positions[i][1] ))
    # Draw Pac-Man
    game_canvas.blit(pacman_dir_img, (pacman_position[0] - 16, pacman_position[1] - 16))
    
    

    #Rescale screen to fit game window
    draw_text(f"Score: " + str(score) + "     Lives: " + str(pacman_lives), 25, 400, 10)
    screen.blit(pygame.transform.scale(game_canvas,(SCREEN_WIDTH-20, SCREEN_HEIGHT)), (0,0))

    #Update the display
    if pacman_lives > 0:
        pygame.display.flip()
    else:
        game_canvas.fill(BLACK)
        draw_text("GAME OVER", 50, GAME_W/2-100, GAME_H/2-100)
        screen.blit(pygame.transform.scale(game_canvas,(SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()
    if pellets > 0:
        pass
    else:
        game_canvas.fill(BLACK)
        draw_text("Congrats you win", 50, GAME_W/2-100, GAME_H/2-100)
        screen.blit(pygame.transform.scale(game_canvas,(SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()
        pygame.time.delay(5000)
        running = False
    


# Limit the frame rate
    clock.tick(60)

# Quit the game


pygame.quit()
import pygame
import random

# strucuture
# initialize
pygame.init()

#membuat ukuran display
window_witdh = 800
window_height = 600
window = pygame.display.set_mode((window_witdh, window_height))

pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

#initial snake position
snake_position = [100,50]
snake_body = [[100,50], [90,50], [80,50]]

#food position
food_position = [random.randrange(1, (window_witdh // 10))* 10,
                 random.randrange(1,(window_height // 10))* 10]
food_spawn = True

#initial snake direction
direction = 'right'
change_to = direction

#initial score
score = 0

# Define the clock object to control the frame rate
clock = pygame.time.Clock()

# Define the font object for the score display
font = pygame.font.Font(None, 36)

def game_over():
    #display game over message
    game_over_text = font.render("Game Over!!", True, white)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.midtop = (window_witdh / 2, window_height / 4)
    window.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

while True:
    # user input / database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'right'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'left'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'up'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'down'
                
    # Validate the direction
    if change_to == 'right' and not direction == 'left':
        direction = 'right'
    if change_to == 'left' and not direction == 'right':
        direction = 'left'
    if change_to == 'up' and not direction == 'down':
        direction = 'up'
    if change_to == 'down' and not direction == 'up':
        direction = 'down'

    #update snake direction
    if direction == 'right':
        snake_position[0] += 10
    if direction == 'left':
        snake_position[0] -= 10
    if direction == 'up':
        snake_position[1] -= 10
    if direction == 'down':
        snake_position[1] += 10
        
    #increase snake body
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    
    #respawn food
    if not food_spawn:
        food_position = [random.randrange(1, (window_witdh // 10))* 10,
                        random.randrange(1,(window_height // 10))* 10]
        food_spawn = True
        
    window.fill(black)
    
    #draw snake
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    #draw food
    pygame.draw.rect(window, red, pygame.Rect(food_position[0], food_position[1], 10, 10))
    
    #game over condition
    if snake_position[0] >= window_witdh or snake_position[0] < 0:
        game_over()
    if snake_position[1] >= window_height or snake_position[1] < 0:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    #display score
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, [10, 10])
    
    # render
    pygame.display.flip()
    
    #control frame rate
    clock.tick(20)
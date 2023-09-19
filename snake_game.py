import pygame
import random

pygame.init()

window_x = 720
window_y = 480

screen = pygame.display.set_mode((window_x, window_y), pygame.RESIZABLE)
pygame.display.set_caption('Snake_Game_Arshad')
fps = pygame.time.Clock()
bg = pygame.image.load("img.png")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


snake_speed = 30
snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]

fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

paused = False

last_spawn = pygame.time.get_ticks()


def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score :' + str(score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)
    fps.tick(60)


def game_over():
    font = pygame.font.SysFont('times new roman', 30)
    game_over_surface = font.render('Your score is :' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    # time.sleep()
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()


# running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_SPACE:
                paused = not paused
                screen.lock()
                fps.tick(0)
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False

    current_time = pygame.time.get_ticks()
    if current_time - last_spawn >= 1000:
        if score <= 0:
            game_over()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
        last_spawn = current_time
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    screen.fill(black)
    screen.blit(bg, (0, 0))

    pygame.draw.rect(screen, red, pygame.Rect(snake_position[0], snake_position[1], 10, 10))
    for pos in snake_body[1:]:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
        if pos[0] > window_x or pos[0] < 0:
            break
        if pos[1] > window_y or pos[1] < 0:
            break


    pygame.draw.rect(screen, blue, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game over conditions

    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)




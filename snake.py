'''
Snake Game  
A simple 2D snake game made with `pygame`.  
The player controls the snake using arrow keys and eats apples to grow.
'''
import pygame, random

pygame.init()
WIDTH, HEIGHT = 400, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(100, 100)]
direction = (20, 0)
apple = (random.randint(0, 19)*20, random.randint(0, 19)*20)

def draw():
    win.fill((0,0,0))
    for s in snake:
        pygame.draw.rect(win, (0,255,0), (*s, 20, 20))
    pygame.draw.rect(win, (255,0,0), (*apple, 20, 20))
    pygame.display.update()

run = True
while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: direction = (0, -20)
    elif keys[pygame.K_DOWN]: direction = (0, 20)
    elif keys[pygame.K_LEFT]: direction = (-20, 0)
    elif keys[pygame.K_RIGHT]: direction = (20, 0)

    new_head = (snake[0][0]+direction[0], snake[0][1]+direction[1])
    snake.insert(0, new_head)
    if new_head == apple:
        apple = (random.randint(0, 19)*20, random.randint(0, 19)*20)
    else:
        snake.pop()
    if new_head in snake[1:] or not 0 <= new_head[0] < WIDTH or not 0 <= new_head[1] < HEIGHT:
        run = False
    draw()
pygame.quit()

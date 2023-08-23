import pygame
import random

pygame.init()

# Initials
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
run = True
direction = [0, 1]
angle = [0, 1, 2]

# Colors
Green = (0, 255, 0)
Blue = (0, 0, 255)
BLACK = (0, 0, 0)

# Ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.2, 0.2

# Paddle Dimensions
paddle_width, paddle_height = 15, 130
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH -(100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0

# Main Loop
while run:
    wn.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_paddle_vel = -0.2
            if event.key == pygame.K_DOWN:
                right_paddle_vel = 0.2
            if event.key == pygame.K_w:
                left_paddle_vel = -0.2
            if event.key == pygame.K_s:
                left_paddle_vel = 0.2

        if event.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    # Ball Collision
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_x, ball_vel_y = -0.4, 0.2
            if ang == 1:
                ball_vel_x, ball_vel_y = -0.2, 0.2
            if ang == 2:
                ball_vel_x, ball_vel_y = -0.2, 0.4
        if dir == 1:
            if ang == 0:
                ball_vel_x, ball_vel_y = 0.4, 0.2
            if ang == 1:
                ball_vel_x, ball_vel_y = 0.2, 0.2
            if ang == 2:
                ball_vel_x, ball_vel_y = 0.2, 0.4
        ball_vel_x *= -1

    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x, ball_vel_y = 0.2, 0.2

        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_x, ball_vel_y = -0.4, 0.2
            if ang == 1:
                ball_vel_x, ball_vel_y = -0.2, 0.2
            if ang == 2:
                ball_vel_x, ball_vel_y = -0.2, 0.4
        if dir == 1:
            if ang == 0:
                ball_vel_x, ball_vel_y = 0.4, 0.2
            if ang == 1:
                ball_vel_x, ball_vel_y = 0.2, 0.2
            if ang == 2:
                ball_vel_x, ball_vel_y = 0.2, 0.4

    # Ball Movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Paddle Collision
    # Left Paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
    # Right Paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1
    

    # Paddle Movement
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    # Object Drawing
    pygame.draw.circle(wn, Green, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, Blue, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, Blue, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update()
import pygame
import sys
import math

pygame.init()

screen_width = 720 / 1.5
screen_height = 1280 / 1.5
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball Animation")

bounce_sound = pygame.mixer.Sound('bounce.wav')

black = (0, 0, 0)
white = (255, 255, 255)
trail_color = (100, 100, 255)

circle_center = (screen_width // 2, screen_height // 2)
circle_radius = 220

ball_radius = 20
ball_color = white
ball_pos = [screen_width // 2, screen_height // 2 - circle_radius + ball_radius]
ball_vel = [5, 5]
gravity = 0.5

trail = []

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_vel[1] += gravity
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    trail.append((ball_pos[0], ball_pos[1], ball_radius))
    if len(trail) > 10:
        trail.pop(0)

    dx = ball_pos[0] - circle_center[0]
    dy = ball_pos[1] - circle_center[1]
    distance = math.sqrt(dx**2 + dy**2)

    if distance >= circle_radius - ball_radius:
        nx = dx / distance
        ny = dy / distance
        ball_pos[0] = circle_center[0] + (circle_radius - ball_radius) * nx
        ball_pos[1] = circle_center[1] + (circle_radius - ball_radius) * ny
        dot_product = ball_vel[0] * nx + ball_vel[1] * ny
        ball_vel[0] -= 2 * dot_product * nx
        ball_vel[1] -= 2 * dot_product * ny
        circle_radius -= 5
        bounce_sound.play()

    screen.fill(black)
    pygame.draw.circle(screen, white, circle_center, circle_radius, 2)

    for pos in trail:
        pos_x, pos_y, radius = pos
        pygame.draw.circle(screen, trail_color, (int(pos_x), int(pos_y)), int(radius))

    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), int(ball_radius))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

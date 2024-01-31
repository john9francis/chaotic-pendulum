# This file is an animated demonstration of a driven-damped pendulum

import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Constants
width, height = 800, 600
fps = 60
dt = 1 / fps

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Pendulum parameters
length = 150
theta = math.pi / 4
omega = 0
alpha = 0
g = 9.81 * 100
damping = 1
amplitude = 1
frequency = 1

# make a list of thetas
thetas = []

# Initialize screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Driven-Damped Pendulum Simulation")

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update pendulum motion equations
    alpha = -g / length * math.sin(theta) - damping * omega + amplitude * math.sin(frequency * pygame.time.get_ticks() / 1000)
    omega += alpha * dt
    theta += omega * dt

    # Draw background
    screen.fill(black)

    # Draw pendulum
    pendulum_x = width // 2 + length * math.sin(theta)
    pendulum_y = height // 2 + length * math.cos(theta)
    pygame.draw.line(screen, white, (width // 2, height // 2), (pendulum_x, pendulum_y), 5)
    pygame.draw.circle(screen, white, (int(pendulum_x), int(pendulum_y)), 15)

    # draw theta graph

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

# Quit pygame
pygame.quit()

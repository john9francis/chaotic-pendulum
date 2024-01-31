# This file is an animated demonstration of a driven-damped pendulum

import pygame
import math

# my own classes
class Theta:
    pos = pygame.Vector2(0.0)
    speed = 50

    def __init__(self, pos) -> None:
        self.pos = pos
        pass
    
    def update(self, dt):
        # always move left
        self.pos.x -= self.speed * dt

        # delete self if leaves screen
        if self.pos.x < 0:
            thetas.remove(self)
        pass
    
    def draw(self, screen):
        pygame.draw.circle(screen, red, (self.pos.x, self.pos.y), 2)
        pass

# Initialize pygame
pygame.init()

# Constants
width, height = 1200, 800
dt = .007

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


# Pendulum parameters
length = 9.8
theta = .2
omega = 0
alpha = 0
g = 9.8
damping = .5
amplitude = 1.2
frequency = 2/3

# make a list of thetas
thetas = []

# Initialize screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Driven-Damped Pendulum Simulation")

# Main loop
clock = pygame.time.Clock()
running = True

time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update pendulum motion equations
    alpha = -g / length * math.sin(theta) - damping * omega + amplitude * math.sin(frequency * time)
    omega += alpha * dt
    theta += omega * dt

    # Draw background
    screen.fill(black)

    # Draw pendulum
    y_shift = 150
    scale_factor = 20

    scaled_length = scale_factor * length

    pendulum_x = width // 2 + scaled_length * math.sin(theta)
    pendulum_y = height // 2 + scaled_length * math.cos(theta) + y_shift
    pygame.draw.line(screen, white, (width // 2, height // 2 + y_shift), (pendulum_x, pendulum_y), 5)
    pygame.draw.circle(screen, white, (int(pendulum_x), int(pendulum_y)), 15)

    # draw theta graph
    theta_pos = pygame.Vector2(width // 2, height // 2 - scaled_length/2 * math.cos(theta) - 200)
    th = Theta(theta_pos)
    thetas.append(th)

    for t in thetas:
        t.update(dt)
        t.draw(screen)

    # Update display
    pygame.display.flip()

    # increment time
    time += dt

# Quit pygame
pygame.quit()

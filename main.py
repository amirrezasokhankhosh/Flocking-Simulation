import pygame
import sys
import random
import numpy as np
from pygame.locals import KEYDOWN, K_q
from boid import Boid
import time


def show_boids():
    for boid in boids:
        pos = boid.pos
        pygame.draw.circle(screen, WHITE, (int(pos[0, 0]), int(pos[1, 0])), 5)


WIDTH, HEIGHT = 600, 600
GREY = (55, 55, 55)
WHITE = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flocking Simulation")
screen.fill(GREY)

boids = []

for i in range(50):
    pos = np.array([[float(random.randint(0, WIDTH - 1))],
                   [float(random.randint(0, HEIGHT - 1))]])
    velocity = np.random.rand(2, 1)
    acsseleration = np.random.rand(2, 1)
    boid = Boid(pos, velocity, acsseleration)
    boids.append(boid)

show_boids()
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()
    time.sleep(.1)
    for boid in boids:
        boid.update()
    screen.fill(GREY)
    show_boids()
    pygame.display.update()

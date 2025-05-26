import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 255), self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, asteroid_field):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rad = self.radius - ASTEROID_MIN_RADIUS
        pos = self.position
        rand_angle = random.uniform(20, 50)
        vector = self.velocity * 1.2
        vel1 = vector.rotate(rand_angle)
        vel2 = vector.rotate(-rand_angle)
        asteroid_field.spawn(rad, pos, vel1)
        asteroid_field.spawn(rad, pos, vel2)
            
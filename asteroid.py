import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        vel1 = pygame.math.Vector2.rotate(self.velocity, new_angle) * 1.2
        vel2 = pygame.math.Vector2.rotate(self.velocity, -new_angle) * 1.2

        return [(new_radius, self.position, vel1), (new_radius, self.position, vel2)]


        


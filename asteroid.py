import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,                  # The surface to draw on
            "white",                 # The color of the circle
            self.position,           # Center position (Vector2)
            self.radius,             # Radius
            LINE_WIDTH               # Line width from constants
        )
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = new_velocity1*1.2
            asteroid2.velocity = new_velocity2*1.2

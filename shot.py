import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH


class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
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

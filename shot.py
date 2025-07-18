from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt
        if not (0 <= self.position.x <= SCREEN_WIDTH and 0 <= self.position.y <= SCREEN_HEIGHT):
            self.kill()  # Remove shot if it goes off-screen

    def draw(self, surface):
        pygame.draw.circle(surface, (255,255,255), (int(self.position.x), int(self.position.y)), self.radius)
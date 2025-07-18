from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
import pygame

# Player class for the game
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)

    def rotate(self, dt):
        # Rotate the player based on input direction and turn speed
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360

    def update(self, dt):
        # Update player position based on velocity
        self.position += self.velocity * dt
    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
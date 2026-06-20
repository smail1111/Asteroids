from logger import *
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        ran = random.uniform(30,50)
        vector1= self.velocity.rotate(ran)
        vector2 = self.velocity.rotate(-ran)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0], self.position[1],new_radius)
        new_asteroid1.velocity = vector1 * 1.2
        new_asteroid2 = Asteroid(self.position[0], self.position[1],new_radius)
        new_asteroid2.velocity = vector2 * 1.2
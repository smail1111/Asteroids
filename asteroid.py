from power import *
from logger import *
from constants import *
from circleshape import *
from explosion import *
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        exposion = Explosion(self.position[0], self.position[1],self.radius)
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

        ran = random.randint(1, POWER_DROP_CHANCE + 2)
        
        if ran == POWER_DROP_CHANCE:
            power = TripleShot(self.position[0], self.position[1])
        elif ran == POWER_DROP_CHANCE + 1:
            power = Shield(self.position[0], self.position[1]) 
        elif ran == POWER_DROP_CHANCE + 2:
            power = Speed_Boost(self.position[0], self.position[1])
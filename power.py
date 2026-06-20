from circleshape import *
from constants import *

class Power(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,POWER_RADIUS)
        self.lifespan = POWER_LIFESPAN
    
    def draw(self, screen):
        pygame.draw.circle(screen,"yellow",self.position,self.radius)

    def update(self, dt):
        if self.lifespan < 0:
            self.kill()
        self.lifespan -= dt
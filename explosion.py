from circleshape import *
from constants import *

class Explosion(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.lifespan = EXPLOSION_LIFESPAN

    def draw(self, screen):
        pygame.draw.circle(screen,"orange",self.position,self.radius)
 
    def update(self, dt):
        if self.lifespan < 0:
            self.kill()
        self.lifespan -= dt
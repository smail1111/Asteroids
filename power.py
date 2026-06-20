from circleshape import *
from constants import *

class Power(CircleShape):
    def __init__(self,x,y,color):
        super().__init__(x,y,POWER_RADIUS)
        self.lifespan = POWER_LIFESPAN
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen,self.color,self.position,self.radius)

    def update(self, dt):
        if self.lifespan < 0:
            self.kill()
        self.lifespan -= dt
    
    def collect_power(self, player):
        pass

class TripleShot(Power):
    def __init__(self,x,y):
        super().__init__(x,y,"yellow")

    def collect_power(self, player):
        self.kill()
        player.have_triple_shot = True
        player.triple_shot_duration = TRIPLE_SHOT_DURATION

class Shield(Power):
    def __init__(self,x,y):
        super().__init__(x,y,"lightblue")

    def collect_power(self, player):
        self.kill()
        player.have_shield = True
from shot import *
from constants import *
from circleshape import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
        self.timer = 0.0
        
        self.have_speed_boost = False
        self.speed_boost_duration = 0
        
        self.have_triple_shot = False
        self.triple_shot_duration = 0
        
        self.have_shield = False
    
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, "yellow", self.triangle(), LINE_WIDTH)
        if self.have_shield:
            pygame.draw.circle(screen, "lightblue", self.position, self.radius*1.5,2)

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.timer < 0:
                if self.have_triple_shot:
                    self.triple_shot()
                    self.timer = PLAYER_SHOOT_COOLDOWN_SECONDS
                else:
                    self.shoot()
                    self.timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        self.timer -= dt
    
        if self.position[0] < 0:
            self.position[0] = 1280
        if self.position[0] > 1280:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = 720
        if self.position[1] > 720:
            self.position[1] = 0
        
        if self.triple_shot_duration < 0:
            self.have_triple_shot = False
        else:
            self.triple_shot_duration -= dt
    
        if self.speed_boost_duration < 0:
            self.have_speed_boost = False
        else:
            self.speed_boost_duration -= dt
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        
        self.position += rotated_with_speed_vector * 2 if self.have_speed_boost else rotated_with_speed_vector

    def shoot(self):
        
        shot = Shot(self.position[0], self.position[1])
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity *= PLAYER_SHOT_SPEED

    def triple_shot(self):
        shot0 = Shot(self.position[0], self.position[1])
        shot0.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot0.velocity *= PLAYER_SHOT_SPEED

        range = 20
    
        shot1 = Shot(self.position[0], self.position[1])
        shot1.velocity = pygame.Vector2(0, 1).rotate(self.rotation).rotate(range)
        shot1.velocity *= PLAYER_SHOT_SPEED

        shot2 = Shot(self.position[0], self.position[1])
        shot2.velocity = pygame.Vector2(0, 1).rotate(self.rotation).rotate(-range)
        shot2.velocity *= PLAYER_SHOT_SPEED
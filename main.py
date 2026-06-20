import sys
from shot import *
from asteroidfield import *
from asteroid import *
from player import *
from logger import *
from constants import *

import pygame

def main():
    pygame.init()
    pygame.display.set_caption('Asteroids')
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0.0
    
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    player = Player(x, y)
    
    asteroidfield = AsteroidField()
    
    score = 0
    health = 3
    
    font = pygame.font.Font('freesansbold.ttf', 48)
    
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for sprite in updatable:
            sprite.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with_player(player):
                log_event("player_hit")
                health -= 1
                asteroid.kill()
                if health < 1:
                    print("Game Over!")
                    print(f"Score: {score}")
                    sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score += 50
        
        for sprite in drawable:
            sprite.draw(screen)
        
        score += 1
        
        health_text = font.render(f'Health: {health}', True, "white")
        textRect = health_text.get_rect()
        textRect.center = (150,50)
        
        score_text = font.render(f'Score: {score}', True, "white")
        textRect2 = score_text.get_rect()
        textRect2.center = (1130,50)
        
        screen.blit(health_text, textRect)
        screen.blit(score_text, textRect2)
        
        pygame.display.flip()
        
        dt = clock.tick(30) / 100

if __name__ == "__main__":
    main()
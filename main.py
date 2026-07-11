import sys
from power import *
from shot import *
from asteroidfield import *
from asteroid import *
from player import *
from logger import *
from constants import *
from explosion import *
import pygame

#SETTING GLOBAL INITIALS
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Asteroids")

title_font = pygame.font.Font('freesansbold.ttf', 150)

font = pygame.font.Font('freesansbold.ttf', 50)

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

def main():
    # TITLE SCREEN LOOP
    while True:

        log_state()

        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            run_asteroids()


        title_text = title_font.render(f'Asteroids', True, "white")
        textRect1 = title_text.get_rect()
        textRect1.center = (x, y-100)

        play_text = font.render(f'Press Enter to Play', True, "white")
        textRect0 = play_text.get_rect()
        textRect0.center = (x, y+75)

        screen.blit(title_text, textRect1)
        screen.blit(play_text, textRect0)


        pygame.display.flip()


def run_asteroids():

    #SETTING GAME INITIALS
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0.0

    powers = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Power.containers = (powers, updatable, drawable)
    Explosion.containers = (updatable, drawable)

    player = Player(x, y)

    asteroidfield = AsteroidField()

    score = 0
    health = PLAYER_HEALTH


    running = True

    #GAME LOOP
    while running:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill("black")

        for sprite in updatable:
            sprite.update(dt)

        score += dt * 3

        for asteroid in asteroids:


            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")

                    asteroid.split()
                    shot.kill()
                    score += 50

            if asteroid.collides_with_player(player):
                log_event("player_hit")

                if player.have_shield:
                    player.have_shield = False
                else:
                    health -= 1

                asteroid.kill()
                Explosion(asteroid.position[0], asteroid.position[1], asteroid.radius)

                if health < 1:
                    print("You Died!")
                    print(f"Score: {score:.0f}")
                    running = False


        for power in powers:
            if power.collides_with_player(player):
                power.collect_power(player)

        for sprite in drawable:
            sprite.draw(screen)

        health_text = font.render(f'Health: {health}', True, "white")
        textRect = health_text.get_rect()
        textRect.center = (150,50)

        score_text = font.render(f'Score: {score:.0f}', True, "white")
        textRect2 = score_text.get_rect()
        textRect2.center = (1130,50)

        screen.blit(health_text, textRect)
        screen.blit(score_text, textRect2)

        dt = clock.tick(60) / 100
    
        pygame.display.flip()


    while True:
        #GAME OVER SCREEN LOOP
        log_state()

        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            run_asteroids()

        death_text = font.render(f'You Died!', True, "white")
        textRect1 = death_text.get_rect()
        textRect1.center = (x, y-75)

        retry_text = font.render(f'Retry: Enter', True, "white")
        textRect0 = retry_text.get_rect()
        textRect0.center = (x, y+75)

        textRect2.center = (x,y)

        screen.blit(death_text, textRect1)
        screen.blit(retry_text, textRect0)
        screen.blit(score_text, textRect2)

        pygame.display.flip()


#CALL MAIN
if __name__ == "__main__":
    main()
import pygame
from constants import *
from player import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
                
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000
        for game_object in updatable:
            game_object.update(dt)
        for game_object in drawable:
            game_object.draw(screen)
        pygame.display.flip()
        for asteroid in asteroids:
            if asteroid.get_collision(player) == True:
                print(f"Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.get_collision(shot) == True:
                    new_asteroids = asteroid.split()
                    if new_asteroids:
                        for new_radius, new_pos, new_vel in new_asteroids:
                            asteroid_field.spawn(new_radius, new_pos, new_vel)
                    shot.kill()


if __name__ == "__main__":
        main()


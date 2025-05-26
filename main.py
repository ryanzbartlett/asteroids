import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    field = AsteroidField()

    score_font = pygame.font.SysFont(None, 24)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        for sprite in drawable:
            sprite.draw(screen)

        # UI
        img = score_font.render(f"Score: {score * 100}", True, (255, 255, 255))
        screen.blit(img, (20, 20))

        pygame.display.flip()

        dt = clock.tick(60.0) / 1000
        updatable.update(dt)

        for asteroid in asteroids:
            if player.isColliding(asteroid):
                print("Game over!")
                exit(0)

            for shot in shots:
                if shot.isColliding(asteroid):
                    score += 1
                    shot.kill()
                    asteroid.split(field)


if __name__ == "__main__":
    main()

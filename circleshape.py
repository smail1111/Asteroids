import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    def collides_with(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        return self.radius + other.radius >= distance

    def collides_with_player(self, player):
        vector0 = pygame.math.Vector2.distance_to(self.position, player.triangle()[0])
        vector1 = pygame.math.Vector2.distance_to(self.position, player.triangle()[1])
        vector2 = pygame.math.Vector2.distance_to(self.position, player.triangle()[2])

        return self.radius >= vector0 or self.radius >= vector1 or self.radius >= vector2
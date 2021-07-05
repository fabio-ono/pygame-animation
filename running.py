import pygame
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.animating = False
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('assets/mario-2.png'))
        self.sprites.append(pygame.image.load('assets/mario-3.png'))
        self.sprites.append(pygame.image.load('assets/mario-4.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.animating = True

    def not_animate(self):
        self.animating = False

    def update(self):
        if self.animating:
            self.current_sprite += 0.20

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]


# setup pygame
pygame.init()
clock = pygame.time.Clock()

# screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Animation")

# sprite
moving_sprites = pygame.sprite.Group()
player = Player(130, 200)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.animate()
            if event.key == pygame.K_ESCAPE:
                player.not_animate()

    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)

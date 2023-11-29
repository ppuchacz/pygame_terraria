from typing import Tuple

from pygame import Surface
import pygame


IMAGE_PATH = 'character.png'

charatcer_idle_image: pygame.Surface = pygame.image.load(IMAGE_PATH)

class Character:
    def __init__(self, position: Tuple[float, float], items = []) -> None:
        self.spawn(position, items)

    def spawn(self, position: Tuple[float, float], items = []) -> None:
        self.position = position
        self.items = items

    def render(self, surface: Surface) -> None:
        if not self.is_spawned():
            return

        surface.blit(charatcer_idle_image, self.position)

    def is_spawned(self) -> bool:
        return self.position != None
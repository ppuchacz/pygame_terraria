import pygame

UI_SCALE = 2.0
UI_FRAME_SIZE = 32
UI_ITEM_SIZE = 16

FRAME_SPACING = 10

EQ_LIST_POSITION = (0, 0)

BLOCK_GRASS = 1
BLOCK_DIRT = 2
BLOCK_STONE = 3

ITEMS = {
    1: BLOCK_GRASS,
    2: BLOCK_DIRT,
    3: BLOCK_STONE,
}

asset_path = {
    'grass' : "grass.png",
    'dirt' : "dirt.png",
    'stone' : "stone.png",
    'frame': 'frame.png',
    'frame-fill': 'frame-fill.png',
}


def load_image(path: str, size: int = 32, opaque: float = 1.0):
    image: pygame.Surface = pygame.image.load(path)
    if opaque < 1.0:
        image.fill((255, 255, 255, opaque * 255), special_flags=pygame.BLEND_RGBA_MULT)
    return pygame.transform.scale(image, (int(size * UI_SCALE), int(size * UI_SCALE)))

ASSET_FRAME_ID = 201
ASSET_FRAME_FILL_ID = 202

assets = {
    1: load_image(asset_path['grass'], UI_ITEM_SIZE),
    2: load_image(asset_path['dirt'], UI_ITEM_SIZE),
    3: load_image(asset_path['stone'], UI_ITEM_SIZE),
    ASSET_FRAME_ID: load_image(asset_path['frame'], UI_FRAME_SIZE),
    ASSET_FRAME_FILL_ID: load_image(asset_path['frame-fill'], UI_FRAME_SIZE),
}


def items_frame(items: list, surface: pygame.Surface, selected: int) -> None:
    for i, item_id in enumerate(items):
        position = [EQ_LIST_POSITION[0] + i * UI_FRAME_SIZE * UI_SCALE, EQ_LIST_POSITION[1]]
        if i == selected:
            surface.blit(assets[ASSET_FRAME_FILL_ID], position)
        else:
            surface.blit(assets[ASSET_FRAME_ID], position)
        if item_id == 0:
            continue

        center = (
            position[0] + (UI_FRAME_SIZE * UI_SCALE / 2) - (UI_ITEM_SIZE * UI_SCALE / 2),
            position[1] + (UI_FRAME_SIZE * UI_SCALE / 2) - (UI_ITEM_SIZE * UI_SCALE / 2),
        )
        
        surface.blit(assets[item_id], center)

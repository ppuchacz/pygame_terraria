from typing import List, Tuple


def point_rect(point: Tuple[int, int], rect: Tuple[int, int, int, int]) -> bool:
    point_x = point[0]
    point_y = point[1]
    rect_x = rect[0]
    rect_y = rect[1]
    rect_width = rect[2]
    rect_height = rect[3]

    rect_right_border_x = rect_x + rect_width
    rect_bottom_border_y = rect_y + rect_height

    return point_x >= rect_x and point_x <= rect_right_border_x and point_y >= rect_y and point_y <= rect_bottom_border_y

def get_board_element_pointed_by(point: Tuple[int, int], block_size: int) -> Tuple[int, int]:
    point_x = point[0]
    point_y = point[1]

    return ((int)(point_x / block_size), (int)(point_y / block_size))

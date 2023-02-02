from typing import List, Tuple


# unused
def list_dimensions_num(list: List):
    if len(list) > 0 and isinstance(list[0], Tuple):
        return list_dimensions_num(list)
    
    return 1


def create_list(size: tuple, value = None) -> List:
    this_size = size[0]
    list = []

    if len(size) > 1:
        for i in range(this_size):
            list.append(create_list(size[1:], value))
        
        return list
    
    for i in range(this_size):
        list.append(value)

    return list
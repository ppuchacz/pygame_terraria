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


def keep_in_range(value, minimum, maximum):
    value = min(value, maximum)
    value = max(value, minimum)
    return value


def keep_in_range_tuple(values: tuple, minimum: tuple, maximum: tuple) -> tuple:
    output_values = []
    for i in range(len(values)):
        output_values.append(keep_in_range(values[i], minimum[i], maximum[i]))

    return tuple(output_values)
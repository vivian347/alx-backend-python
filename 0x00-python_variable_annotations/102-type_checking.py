#!/usr/bin/env python3
from typing import Tuple, List

"""Function"""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """mypy for type checking"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

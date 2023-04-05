#!/usr/bin/env python3
from typing import List, Union

"""type-annotated function sum_mixed_list"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a mixed lsit of integers and floats and returns sum as float"""
    sum = 0
    for x in mxd_lst:
        sum += x

    return sum

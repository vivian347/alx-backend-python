#!/usr/bin/env python3
from typing import List

"""type-annotated fn of lists"""


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats and returns the sum"""
    sum = 0
    for x in input_list:
        sum += x
    return sum

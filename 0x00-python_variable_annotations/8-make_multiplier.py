#!/usr/bin/env python3
from typing import Callable

"""type annotated fn make_multiplier"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as arg and returns a fn that multiples a float by multiplier"""
    def multiplier_func(num: float) -> float:
        return num * multiplier
    return multiplier_func

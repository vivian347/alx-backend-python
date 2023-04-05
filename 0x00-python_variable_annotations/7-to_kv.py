#!/usr/bin/env python3
from typing import List, Tuple, Union

"""Type-annotated fn to_kv"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of a str k and square of v"""
    return k, v ** 2

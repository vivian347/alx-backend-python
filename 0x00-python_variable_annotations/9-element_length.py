#!/usr/bin/env python3
from typing import List, Iterable, Sequence, Tuple

"""type-annotated duck function"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """lst is an itearble sequence and the fn returns a list of tuples"""
    return [(i, len(i)) for i in lst]

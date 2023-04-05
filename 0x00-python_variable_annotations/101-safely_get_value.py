#!/usr/bin/env python3

from typing import Union, TypeVar, Mapping, Any

"""TypeVar function"""

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """TypeVar"""
    if key in dct:
        return dct[key]
    else:
        return default

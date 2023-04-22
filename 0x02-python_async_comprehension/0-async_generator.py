#!/usr/bin/env python3

"""async_generator"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loop 10 times, async wait 1 second,
    yiels a random number between 0 ans 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

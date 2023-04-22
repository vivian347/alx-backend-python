#!/usr/bin/env python3

"""async_generator"""

import asyncio
from random import uniform


async def async_generator():
    """loop 10 times, async wait 1 second,
    yiels a random number between 0 ans 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

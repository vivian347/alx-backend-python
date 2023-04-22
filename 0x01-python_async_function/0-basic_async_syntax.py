#!/usr/bin/env python3
"""0-basic_async_syntax"""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """takes int and waits for a random delay between 0 and the int"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

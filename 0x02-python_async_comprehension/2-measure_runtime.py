#!/usr/bin/env python3

"""measure_runtime"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in
    parallel using asyncio.gather."""
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    total_time = end_time - start_time
    return total_time

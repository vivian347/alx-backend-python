#!/usr/bin/env python3
"""multiple couroutines at the same time"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n times in ascending order"""
    delay_list = []
    tasks = []

    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        j = 0
        while j < len(delay_list) and delay > delay_list[j]:
            j += 1
        delay_list.insert(j, delay)
    return delay_list

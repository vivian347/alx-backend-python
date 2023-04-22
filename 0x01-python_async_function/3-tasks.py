#!/usr/bin/env python3

"""task_wait_random"""

from typing import TypeVar
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

# Define a type variable T that can only be bound to an instance of asyncio.Task
T = TypeVar('T', bound=asyncio.Task)


def task_wait_random(max_delay: int) -> T:
    """takes in max_delay and returns a asyncio.Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task

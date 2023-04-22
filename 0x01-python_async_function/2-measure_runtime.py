#!/usr/bin/env python3
"""measures total execution time for wait_n"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ total execution time for
    wait_n(n, max_delay), and returns total_time / n"""
    start_time = time.time()
    result = asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n

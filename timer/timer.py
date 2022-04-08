import time
import numpy as np


def time_func(func, *args, n_loops=100, factor=1e6, label='μs', precision=3):
    times = np.zeros(n_loops)
    for i in range(n_loops):
        start = time.time()
        func(*args)
        times[i] = time.time() - start
    return {
        'name': func.__name__,
        'loops': n_loops,
        f'mean ({label})': round(times.mean() * factor, precision),
        f'std ({label})': round(times.std() * factor, precision)
    }

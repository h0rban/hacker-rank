import time
import numpy as np


def time_func(func, *args, n_loops=100):
    times = np.zeros(n_loops)
    for i in range(n_loops):
        start = time.time()
        func(*args)
        times[i] = time.time() - start
    return {
        'name': func.__name__,
        'mean': times.mean(),
        'std': times.std()
    }

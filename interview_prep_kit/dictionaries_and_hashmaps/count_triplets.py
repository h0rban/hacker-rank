import math
from collections import Counter


def count_triplets(arr, r):
    """
    https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

    completed on 2021-10-30

    note: this version exceeds the time limit, can use n * r instead of n + 1 if not doing log
    """
    cnt, d, pairs, arr = 0, Counter(), Counter(), [int(math.log(x, r)) for x in arr]
    for n in reversed(arr):
        if n + 1 in pairs:
            cnt += pairs[n + 1]
        if n + 1 in d:
            pairs[n] += d[n + 1]
        d[n] += 1
    return cnt

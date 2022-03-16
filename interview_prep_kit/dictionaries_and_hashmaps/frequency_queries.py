from collections import Counter


def freq_query(queries):
    """
    https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps

    completed on 2021-10-29
    """
    freq, cnt, out = Counter(), Counter(), []
    for q, n in queries:
        if q == 1:
            if n in freq:
                cnt[freq[n]] -= 1
            freq[n] += 1
            cnt[freq[n]] += 1
        elif q == 2 and n in freq and freq[n] > 0:
            cnt[freq[n]] -= 1
            freq[n] -= 1
            cnt[freq[n]] += 1
        elif q == 3:
            out.append(1 if n in cnt and cnt[n] > 0 else 0)
    return out

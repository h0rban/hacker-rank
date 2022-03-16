def minimum_bribes(q):
    """
    https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

    completed on 2021-10-28
    """

    moves, q = 0, [p - 1 for p in q]
    for i, P in enumerate(q):
        if P - i > 2:
            return -1
        for j in range(max(P - 1, 0), i):
            if q[j] > P:
                moves += 1
    return moves

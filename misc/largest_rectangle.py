def largest_rectangle_v1(hs):
    # too slow
    max_area = 0
    for i in range(len(hs)):
        for k in range(1, len(hs) - i + 1):
            area = k * min(hs[i: i + k])
            if area > max_area:
                max_area = area
    return max_area


def largest_rectangle_v2(hs):
    # too slow - uses DP instead of getting min all the time
    n = len(hs)
    mins, maxs = [0] * n, [0] * n
    for i in range(n):
        h = hs[i]
        for j in range(i + 1):
            if i == j:
                mins[j] = h
                maxs[j] = h
            else:
                mins[j] = min(mins[j], h)
                maxs[j] = max(maxs[j], mins[j] * (i + 1 - j))
    return max(maxs)


def largest_rectangle(hs):
    """
    https://www.hackerrank.com/challenges/largest-rectangle/problem

    explanation: https://youtu.be/ZmnqCZp9bBs

    completed 2022-03-11

    """

    stack, area, i = [], 0, 0

    def update_area(index):
        m = hs[stack.pop()]
        n = index
        if stack:
            n = index - stack[-1] - 1
        return max(area, m * n)
    while i < len(hs):
        if not stack or hs[stack[-1]] <= hs[i]:
            stack.append(i)
            i += 1
        else:
            area = update_area(i)
    while stack:
        area = update_area(i)
    return area

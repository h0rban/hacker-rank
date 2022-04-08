def equal_stacks(h0, h1, h2):
    def get_idx_max(arr):
        val_max = max(arr)
        for i in range(len(heights)):
            if heights[i] == val_max:
                return i

    stacks = [h0, h1, h2]

    if not all(map(bool, stacks)):
        return 0

    heights = list(map(sum, stacks))
    while not (heights[0] == heights[1] == heights[2]):
        idx_max = get_idx_max(heights)
        heights[idx_max] -= stacks[idx_max].pop(0)

    return heights[0]


def equal_stacks_v2(h0, h1, h2):
    stacks = [h0, h1, h2]

    if not all(map(bool, stacks)):
        return 0

    heights = list(map(sum, stacks))
    while h0 and h1 and h2:

        if heights[0] == heights[1] == heights[2]:
            return heights[0]

        m = min(heights)
        for i in range(len(heights)):
            while heights[i] > m:
                heights[i] -= stacks[i].pop(0)

    return 0

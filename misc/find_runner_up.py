def find_second(iterable, maximum=True, default=None):
    if default is None:
        default = float('-inf') if maximum else float('inf')
    m, m2 = default, default
    func_main, func_secondary = (max, min) if maximum else (min, max)
    for n in iterable:
        if m != n:
            m2 = func_main(m2, func_secondary(m, n))
        m = func_main(m, n)
    return m2


def find_runner_up(arr):  # , min_value=-101):
    """
    https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

    completed on 2022-03-10
    """

    # m, m2 = min_value, min_value
    # for n in arr:
    #     if m != n:
    #         m2 = max(m2, min(m, n))
    #     m = max(m, n)
    # return m2

    return find_second(arr, default=-101)


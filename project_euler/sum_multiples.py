def arithmetic_sum(a, d, n):
    """

    :param a: first term
    :param d: difference between terms
    :param n: number of terms
    :return: arithmetic sum of n terms starting at a and increasing by d
    """
    return n * (2 * a + d * (n - 1)) // 2


def sum_multiples_of_under(a, limit):
    return arithmetic_sum(a, a, (limit - 1) // a)


def sum_of_multiples(limit, a, b):
    """
    completed on 2022-04-05
    """
    sum_a, sub_b, sum_intersection = map(lambda x: sum_multiples_of_under(x, limit), (a, b, a * b))
    return sum_a + sub_b - sum_intersection

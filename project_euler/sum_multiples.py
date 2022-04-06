def arithmetic_sum(first_term, difference, n_terms):
    return n_terms * (2 * first_term + difference * (n_terms - 1)) // 2


def sum_multiples_of_under(first_term, upper_bound):
    return arithmetic_sum(first_term, first_term, (upper_bound - 1) // first_term)


def sum_of_multiples(upper_bound, a, b):
    """
    completed on 2022-04-05
    """
    sum_a, sub_b, sum_intersection = map(lambda x: sum_multiples_of_under(x, upper_bound), (a, b, a * b))
    return sum_a + sub_b - sum_intersection


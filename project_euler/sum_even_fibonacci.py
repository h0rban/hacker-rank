from math import sqrt, floor, log
from decimal import Decimal, Context, setcontext


def sum_even_fibonacci_v1(limit):
    a, b = 0, 1
    total = 0
    while b < limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total


def sum_even_fibonacci_v2(limit):
    a, b = 0, 2
    total = 0
    while b < limit:
        total += b
        a, b = b, 4 * b + a
    return total


def sum_even_fibonacci_v3(limit):
    """
    completed on 2022-04-04
    resources used: https://medium.com/@TheZaki/project-euler-2-even-fibonacci-numbers-2219e9438970
    """
    context = Context(prec=21)
    setcontext(context)

    phi = Decimal(1 + Decimal(5).sqrt()) / Decimal(2)
    psi = Decimal(1 - Decimal(5).sqrt()) / Decimal(2)

    def reverse_fib(fn):
        return floor(log((fn * sqrt(5) + sqrt(5 * (fn ** 2) - 4)) / 2, phi))

    def get_k(n):
        return reverse_fib(n) // 3

    def sum_even(k):
        phi3 = context.power(phi, 3)
        psi3 = context.power(psi, 3)
        return round((Decimal(1) / Decimal(5).sqrt()) * (
                phi3 * ((1 - context.power(phi3, k)) / (1 - phi3)) -
                psi3 * ((1 - context.power(psi3, k)) / (1 - psi3))
        ))

    return sum_even(get_k(limit))

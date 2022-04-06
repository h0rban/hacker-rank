import math


def max_prime_factor(n):
    """
    completed on 2022-04-06
    resources used: https://www.geeksforgeeks.org/find-largest-prime-factor-number/
    """

    def while_divisible(number, divisor, current_max):

        if number % divisor != 0:
            return number, current_max

        while number % divisor == 0:
            number /= divisor

        return number, divisor

    max_prime = -1
    n, max_prime = while_divisible(n, 2, max_prime)  # n must be odd at this point
    n, max_prime = while_divisible(n, 3, max_prime)

    # now we have to iterate only for integers who does not have prime factor 2 and 3
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if i > n:
            break
        n, max_prime = while_divisible(n, i, max_prime)
        n, max_prime = while_divisible(n, i + 2, max_prime)

    # This condition is to handle the case when n is a prime number greater than 4
    if n > 4:
        max_prime = n

    return int(max_prime)

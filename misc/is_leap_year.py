def is_leap_year(y):
    """
    https://www.hackerrank.com/challenges/write-a-function/problem

    completed on 2022-01-18
    """
    return bool(not y % 4 and (not y % 400 or y % 100))

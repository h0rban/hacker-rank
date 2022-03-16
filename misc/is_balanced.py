def is_balanced(s):
    """
    https://www.hackerrank.com/challenges/balanced-brackets/problem

    completed on 2021-11-12
    """
    stack, opposite = [], {'(': ')', '{': '}', '[': ']'}

    for c in s:
        if c in opposite:
            stack.append(c)
        elif not stack or c != opposite[stack.pop()]:
            return False

    return not stack

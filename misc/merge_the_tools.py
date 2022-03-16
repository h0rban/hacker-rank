def merge_the_tools(string, k):
    """
    https://www.hackerrank.com/challenges/merge-the-tools/problem

    completed on 2021-11-10
    """
    out = []
    for i in range(int(len(string) / k)):
        sub = string[i * k: (i + 1) * k]
        out.append(''.join(dict.fromkeys(sub)))
    return out

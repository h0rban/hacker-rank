from collections import Counter


def sherlock_anagrams(s, log=False):
    """
    https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps

    completed on 2021-10-29
    """
    if log:
        print('\n', s)

    def are_anagrams(s1, s2):
        return Counter(s1) == Counter(s2)

    counter = 0
    for sub_length in range(1, len(s)):
        sub_strings = [s[i: i + sub_length] for i in range(len(s) - sub_length + 1)]

        anagrams = []
        for i in range(len(sub_strings) - 1):
            for j in range(i + 1, len(sub_strings)):
                if are_anagrams(sub_strings[i], sub_strings[j]):
                    counter += 1
                    anagrams.append({i: sub_strings[i], j: sub_strings[j]})

        if log:
            print(sub_length, sub_strings, anagrams)

    return counter

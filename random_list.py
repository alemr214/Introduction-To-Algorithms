from random import randint


def make_random_list(n):
    return [randint(1, 100) for _ in range(n)]

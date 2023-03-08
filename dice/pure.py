from typing import DefaultDict
from collections import defaultdict
from random import randrange


Storage = DefaultDict[int, float]


def dice_simulate(s: int) -> Storage:
    num: int
    storage: Storage = defaultdict(int)

    for _ in range(s):
        num = randrange(1, 7)
        storage[num] += 1.0 / s

    return storage

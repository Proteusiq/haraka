from typing import DefaultDict
from collections import defaultdict

import numpy as np

Storage = DefaultDict[int, float]


def dice_simulate(s: int) -> Storage:
    num: int
    storage: Storage = defaultdict(int)

    for _ in np.arange(s):
        num = np.random.randint(1, 7)
        storage[num] += 1.0 / s

    return storage

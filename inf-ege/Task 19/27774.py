from functools import lru_cache
from math import ceil

def make_moves(heaps):
    a, b = heaps
    return (a - 1, b), (a, b - 1), (ceil(a / 2), b), (a, ceil(b / 2))

@lru_cache(None)

def game(heaps):
    if sum(heaps) <= 20:
        return "WIN"
    if heaps[0] <= 1 or heaps[1] <= 1:
        return 0
    if any(game(move) == "WIN" for move in make_moves(heaps)):
        return "P1"
    if any(game(move) == "P1" for move in make_moves(heaps)):
        return 'B1'
    

for stone in range(11, 10000):
    heaps = (10, stone)
    if game(heaps) is not None and game(heaps) == "B1":
        print(stone, game(heaps))

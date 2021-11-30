from functools import lru_cache

def make_moves(heap):
    if (heap % 2 == 0):
        return (heap // 2), (heap - 1), (heap - 2), (heap - 3), (heap - 4), (heap - 5)
    return (heap - 1), (heap - 2), (heap - 3), (heap - 4), (heap - 5)

@lru_cache(None)

def game(heap):
    if heap < 10:
        return "W"
    if any(game(move) == 'W' for move in make_moves(heap)):
        return "P1"
    if all(game(move) == 'P1' for move in make_moves(heap)):
        return 'B1'

for s in range(100, 1, -1):
    if (game(s) is not None and game(s) == 'B1'):
        print(s)
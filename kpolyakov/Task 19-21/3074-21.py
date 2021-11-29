from functools import lru_cache

def make_moves(heap):
    return (heap + 100), (heap * 2)

@lru_cache(None)

def game(heap):
    if heap >= 1000:
        return "WIN"
    if any(game(move) == "WIN" for move in make_moves(heap)):
        return 'P1'
    if all(game(move) == "P1" for move in make_moves(heap)):
        return 'B1'
    if any(game(move) == 'B1' for move in make_moves(heap)):
        return 'P2'
    if all(game(move) == 'P1' or game(move) == 'P2' for move in make_moves(heap)):
        return 'B2'

for stone in range(1, 1000):
    if (game(stone) is not None) and (game(stone) == 'B2'):
        print(game(stone), stone)

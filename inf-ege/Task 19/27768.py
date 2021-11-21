from functools import lru_cache

def make_moves(heaps):
    a, b = heaps
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 3)

@lru_cache(None)

def game(heaps):
    if sum(heaps) >= 84:
        return "WIN"
    if any(game(move) == 'WIN' for move in make_moves(heaps)):
        return "P1"
    if any(game(move) == 'P1' for move in make_moves(heaps)):
        return "B1"

for stone in range(1, 68):
    heaps = (16, stone)
    if game(heaps) is not None and game(heaps) == 'B1':
        print(stone)
        break
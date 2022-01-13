from functools import lru_cache

def make_moves(heaps):
    a, b = heaps
    return (a + 2, b), (a, b + 2), (a * 3, b), (a, b * 3)

@lru_cache(None)

def game(heaps):
    if sum(heaps) >= 45:
        return 'WIN'
    if any(game(move) == 'WIN' for move in make_moves(heaps)):
        return 'P1'
    if all(game(move) == 'P1' for move in make_moves(heaps)):
        return 'B1'

counter = 0

for K in range(1, 100):
    for S in range(1, 100):
        if ((K + S) > 43): continue
        heaps = (K, S)
        if (game(heaps) == 'B1'):
            counter += 1

print(counter)
from functools import lru_cache

def make_moves(heaps):
    a, b = heaps
    return (a + 1, b), (a + 1, b), (a * 3, b), (a, b * 3)

@lru_cache(None)

def game(heaps):
    if sum(heaps) >= 45:
        return 'W'
    from functools import lru_cache

def make_moves(heaps):
    a, b = heaps
    return (a + 1, b), (a + 1, b), (a * 3, b), (a, b * 3)

@lru_cache(None)

def game(heaps):
    if sum(heaps) >= 45:
        return 'W'
    if any(game(move) == 'W' for move in make_moves(heaps)):
        return 'P1'
    if all(game(move) == 'P1' for move in make_moves(heaps)):
        return 'B1'
    if any(game(move) == 'B1' for move in make_moves(heaps)):
        return 'P2'
    if any(game(move) == 'P1' or game(move) == 'P2' for move in make_moves(heaps)):
        return 'B2'

for s in range(1, 41):
    heaps = (4, s)
    if game(heaps) == 'B1' or game(heaps) == 'B2':
        print(s)
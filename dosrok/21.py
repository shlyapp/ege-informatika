from functools import lru_cache

def make_moves(heap):
    a, b = heap
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)

def game(heap):
    if sum(heap) >= 223:
        return 'WIN'
    if any(game(move) == 'WIN' for move in make_moves(heap)):
        return 'P1'
    if all(game(move) == 'P1' for move in make_moves(heap)):
        return 'B1'
    if any(game(move) == 'B1' for move in make_moves(heap)):
        return 'P2'
    if all(game(move) == 'P1' or game(move) == 'P2' for move in make_moves(heap)):
        return 'B2'

for s in range(1, 206):
    heap = (17, s)
    if game(heap) == 'B2':
        print(s)
        break
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
    if any(game(move) == 'P1' for move in make_moves(heap)):
        return 'B1'

for s in range(1, 206):
    heap = (17, s)
    if game(heap) == 'B1':
        print(s)
        break
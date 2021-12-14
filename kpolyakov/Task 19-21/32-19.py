from functools import lru_cache

def make_moves(heaps):
    a, b = heaps
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)

def game(heaps):
    if sum(heaps) >= 40:
        return "WIN"
    if any(game(move) == "WIN" for move in make_moves(heaps)):
        return "P1"
    if any(game(move) == "P1" for move in make_moves(heaps)):
        return "B1"
    if any(game(move) == "B1" for move in make_moves(heaps)):
        return 'P2'
    if all(game(move) == "P1" or game(move) == "P2" for move in make_moves(heaps)):
        return 'B2'

for s in range(1, 31):
    heap = (9, s)
    if (game(heap) == 'B1'):
        print(s)
        break
    
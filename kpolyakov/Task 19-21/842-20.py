from functools import lru_cache

def make_moves(heaps):
    a, b = heaps
    x = []
    if a > 0: x.append( (a - 1, b) )
    if b > 0: x.append( (a, b - 1) )
    if a > 1: x.append( ((a + 1) // 2, b) )
    if b > 1: x.append( (a, (b + 1) // 2) )
    return x

@lru_cache(None)

def game(heaps):
    if sum(heaps) <= 32:
        return "WIN"
    if any(game(move) == "WIN" for move in make_moves(heaps)):
        return "P1"
    if all(game(move) == "P1" for move in make_moves(heaps)):
        return "B1"
    if any(game(move) == "B1" for move in make_moves(heaps)):
        return "P2"
    if all(game(move) == "P1" or game(move) == "P2" for move in make_moves(heaps)):
        return 'B2'

for s in range(23, 100):
    heaps = (10, s)
    if (game(heaps) == "P2"):
        print(s)
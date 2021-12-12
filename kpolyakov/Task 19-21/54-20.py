from functools import lru_cache

def make_moves(heaps):
    a, b = heaps
    return (a * 4, b), (a, b * 4), (a + 1, b), (a, b + 1)

@lru_cache(None)

def game(heaps):
    if heaps[0] * heaps[1] >= 1056:
        return "WIN"
    if any(game(move) == "WIN" for move in make_moves(heaps)):
        return "P1"
    if all(game(move) == "P1" for move in make_moves(heaps)):
        return "B1"
    if any(game(move) == "B1" for move in make_moves(heaps)):
        return "P2"
    if all(game(move) == "P1" or game(move) == "P2" for move in make_moves(heaps)):
        return "B2"

for s in range(1, 132):
    heaps = (8, s)
    if (game(heaps) == "P2"):
        print(s)
from functools import lru_cache

def make_moves(heap):
    return (heap + 1), (heap * 2)
    
@lru_cache(None)

def game(heap):
    if 30 <= heap <= 45:
        return 'WIN'
    if heap > 45:
        return 'P1'
    if any(game(move) == 'WIN' for move in make_moves(heap)):
        return 'P1'
    if all(game(move) == 'P1' for move in make_moves(heap)):
        return 'B1'

for stone in range(1, 30):
    if (game(stone) is not None):
        print(game(stone), stone)

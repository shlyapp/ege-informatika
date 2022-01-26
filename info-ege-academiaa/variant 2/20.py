from functools import lru_cache

def make_moves(heap):
    return heap + 2, heap + 3, heap * 2

@lru_cache(None)

def game(heap):
    if heap >= 30:
        return 'WIN'
    if any(game(move) == 'WIN' for move in make_moves(heap)):
        return 'P1'
    if all(game(move) == 'P1' for move in make_moves(heap)):
        return 'B1'
    if any(game(move) == 'B1' for move in make_moves(heap)):
        return 'P2'
    if all(game(move) == 'P1' or game(move) == 'P2' for move in make_moves(heap)):
        return 'B2'
    
for heap in range(1, 30):
    if game(heap) == 'P2':
        print(heap)

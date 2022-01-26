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
    
for heap in range(1, 30):
    if game(heap) == 'B1':
        print(heap)
from functools import lru_cache


def make_moves(heap):
    return (heap + 3), (heap * 2)


@lru_cache(None)
def game(heap):
    if heap >= 33:
        return 'WIN'
    if any(game(move) == 'WIN' for move in make_moves(heap)):
        return 'P1'
    if all(game(move) == 'P1' for move in make_moves(heap)):
        return 'B1'


for s in range(1, 33):
    if game(s) == 'B1':
        print(s)
        break

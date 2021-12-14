from functools import lru_cache

def make_moves(heap):
    a = []
    if heap % 2 == 0:
        a.append(heap // 2)
    else:
        a.append(heap - 2)
    if heap % 3 == 0:
        a.append(heap // 3)
    else:
        a.append(heap - 3)
    return a

@lru_cache(None)

def game(heap):
    if heap == 1:
        return "WIN"
    if any(game(move) == "WIN" for move in make_moves(heap)):
        return "P1"
    if all(game(move) == "P1" for move in make_moves(heap)):
        return "B1"
    if any(game(move) == "B1" for move in make_moves(heap)):
        return "P2"
    if all(game(move) == "P1" or game(move) == "P2" for move in make_moves(heap)) and any(game(move) == "P1" for move in make_moves(heap)):
        return 'B2'

for s in range(2, 38):
    if (game(s) == 'B2'):
        print(s)
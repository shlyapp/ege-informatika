from functools import lru_cache

def make_move(heaps):
    a, b = heaps
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)

def game(heaps):
    if sum(heaps) >= 62:
        return "WIN"
    # Если Петя хотя бы одним ходом выиграывает
    if any(game(moves) == 'WIN' for moves in make_move(heaps)):
        return "P1"
    # Если Петя всеми ходами привел Ваню к выигрышной позиции
    if any(game(moves) == 'P1' for moves in make_move(heaps)):
        return "B1"
    
for stone in range(1, 52):
    if game( (10, stone) ) is not None:
        print(stone, game( (10, stone) ))
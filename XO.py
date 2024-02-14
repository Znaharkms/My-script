# Игра: "Крестики нолики"
n = int(input('Введите размер поля (n * n): ')) # - размер поля
hod_igroka, game_over = 1, False
pole_game = [(['-'] * n) for j in range(n)] #- создание пустого поля
count_hod = 0


def proverka(pole_game):
    global game_over
    print_pole_game(pole_game)

    # Проверка по горизонтали
    if pole_game[y].count(symbol) == n:
        print(f'*** Выйграл игрок № 1 - "X" ***' if hod_igroka != 1 else f'*** Выйграл игрок № 2 - "O" ***')
        game_over = True
        return

    # Проверка по-вертикали
    z = len([object() for i in pole_game if i[x] == symbol])
    if z == n:
        print(f'*** Выйграл игрок № 1 - "X" ***' if hod_igroka != 1 else f'*** Выйграл игрок № 2 - "O" ***')
        game_over = True
        return

    # Проверка по диагонали
    z = len([object() for i in range(n) if pole_game[i][i] == symbol]) # cверх лево - низ право
    z2 = len([object() for i in range(n) if pole_game[i][n - i - 1] == symbol])  # низ лево - верх право
    if z == n or z2 == n:
        print(f'*** Выйграл игрок № 1 - "X" ***' if hod_igroka != 1 else f'*** Выйграл игрок № 2 - "O" ***')
        game_over = True
        return3

    # Проверка количества ходов
    if count_hod == n ** 2:
        print('*** Победила Ничья ***')
        game_over = True
        return

    return False

def print_pole_game(pole_game): # - печать поля
    print(f"  {' '.join([str(i) for i in range(n)])}")
    for i in range(n):
        print(f'{i} {" ".join(pole_game[i])}')


print_pole_game(pole_game) # - печать поля

while not game_over:

    if hod_igroka == 1:
        symbol = 'X'
        print('Ход игрока № 1 - "X"')
        x, y = map(int, input('Введите номер столбца и строки через пробел (X, Y):').split())
        if x > n or y > n:
            print('Вы ввели неверные координаты. Повторите')
            continue
        elif pole_game[y][x] != '-':
            print('Клетка занята. Повторите')
            continue
        hod_igroka = 2
    else:
        symbol = 'О'
        print('Ход игрока № 2 - "O"')
        x, y = map(int, input('Введите номер столбца и строки через пробел (X, Y):').split())
        if x > n or y > n:
            print('Вы ввели неверные координаты. Повторите')
            continue
        elif pole_game[y][x] != '-':
            print('Клетка занята. Повторите')
            continue
        hod_igroka = 1

    count_hod +=1
    pole_game[y][x] = symbol

    proverka(pole_game)
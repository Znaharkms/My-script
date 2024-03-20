import random
import gc


class BoardException(Exception):
    pass
    ''' Класс исключений для обработки выстрелов в одну точку,
        а также выстрел за границы доски'''

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"

class RepeatShootError(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку! Ещё выстрел!"


class Board:
    ''' Класс создаёт доски играков, а также проверяет выстрелы по короблям,
    проверяет выстрел за пределы доски, попадания в точки, в которые стрел
    игрок ранее. Удаление подбитого коробля.
    '''
    def __init__(self, size=6, hid=False):
        self.size = size
        self.board_game = []
        self.hid = hid
        self.ships = None

    def createBoard(self):
        self.board_game = [(['0'] * self.size) for j in range(self.size)]
        self.ships = Ship()
        self.ships.random_ship(self.size, self.board_game)
        return self.board_game

    def out(self, d):
        return not((0 <= d[0] < self.size) and (0 <= d[1] < self.size))


    def del_zero_ship(self): # Проверка коробля на полное потопление
        for ind, ship in enumerate(self.ships.set_list_ships):
            if len(ship) == 0:
                self.ships.set_list_ships.pop(ind)
                print('\033[31m>>>Корабль потоплен!<<<\033[0m')



    def сheck_repeat_shot(self, d):
        if d not in self.ships.repeat_dots:
            self.ships.repeat_dots.append(d)
            return False
        return True


    def shoot(self, d):
        x, y = d
        try:
            if self.out(d):
                raise BoardOutException()
        except BoardException as error:
            print('\033[33m')
            print(error)
            print('\033[0m')
            return True
        try:
            if self.сheck_repeat_shot(d):
                raise RepeatShootError
        except RepeatShootError as error:
            print('\033[33m')
            print(error)
            print('\033[0m')
            return True

        for ship in self.ships.set_list_ships:
            for ind, dot in enumerate(ship):
                if d == dot:
                    ship.pop(ind)
                    self.board_game[x][y] = 'X'
                    self.del_zero_ship()
                    print('\033[31mПопал! Ещё один ход!\033[0m')
                    return True

        self.board_game[x][y] = '.'
        print('Мимо!')
        return False



class Ship:
    '''Класс создает корабли в рандомном месте
    и рандомном положении (вертикально или горизонтально'''

    def __init__(self):
        self.listShip = [3, 2, 2, 1, 1, 1, 1]
        self.check_dots = [(-1, -1), (-1,0), (1, -1),
                          (0, -1), (0,0), (0, 1),
                          (-1, 1), (1, 0), (1, 1)]
        self.set_list_ships = [] # Список координат готовых кораблейб точек возле них
        self.temp_dots = []
        self.repeat_dots = []


    def check_ship(self, create_ship):
        try:
            for x, y in self.create_ship: # Цикл точек коробля
                for ch_x, ch_y in self.check_dots: # Проверка коробля
                    if (x + ch_x, y + ch_y) in self.temp_dots:
                        raise StopIteration
        except StopIteration:
            return False
        else:
            return True

    def random_ship(self, size, board_game):
        sz = size
        board_game=board_game
        count_ship = 0
        count_attempt = 0
        while len(self.set_list_ships) != 7:
            while True:
                self.create_ship = []  # создание списка кортежей с координатами rjhj,kz
                vg = random.choice('GV')  # выбор вертикали и горизонтали

                if vg == 'G':  # ПО ГОРИЗОНТАЛИ
                    cur_x = random.randint(0, sz- 1 - self.listShip[count_ship])  # выбор строки
                    cur_y = random.randint(0, sz - 1)

                    for i in range(self.listShip[count_ship]):
                        self.create_ship.append((cur_y, cur_x + i))

                if vg == 'V':  # ПО ВЕРТИКАЛИ
                    cur_x = random.randint(0, sz - 1)  # выбор строки
                    cur_y = random.randint(0, sz - 1 - self.listShip[count_ship])

                    for i in range(self.listShip[count_ship]):
                        self.create_ship.append((cur_y + i, cur_x))

                if self.check_ship(self.create_ship):
                    self.set_list_ships.append(self.create_ship) # Добавление коробля в общий список
                    count_ship += 1

                    for i in self.create_ship:
                        self.temp_dots.append(i)
                    break

                if count_attempt == 1000:
                    count_ship = 0
                    count_attempt = 0
                    self.set_list_ships.clear()
                    self.temp_dots.clear()
                count_attempt += 1

        for ship in self.set_list_ships:
            for x, y in ship:
                board_game[x][y] = '■'
        return board_game



class Players:
    '''Класс играков. Печатает поля играков. Запрашивает ходы.'''

    def __init__(self, board=None):
        self.board = Board()
        self.board.createBoard()

    def __str__(self):
        res = ''
        if self.__class__.__name__ == 'PC':
            res += f'Игровое поле Компьютера (Осталось: {len(self.board.ships.set_list_ships)} {self.writing_ending()})\n'
            self.board.hid = True
        else:
            res += f'Игровое поле Игрока (Осталось: {len(self.board.ships.set_list_ships)} {self.writing_ending()})\n'

        res += f"  {' | '.join([str(i + 1) for i in range(self.board.size)])}\n"
        for i in range(self.board.size):
            res += f'{i + 1} {" | ".join(self.board.board_game[i])}\n'

        res += '-' * 23 #+ '\n'

        if self.board.hid: #если у доски статус hid = True, то меняем значек коробля ■ на 0.
            res = res.replace("■", "0")
        return res

    def writing_ending(self):
        if len(self.board.ships.set_list_ships) in [0, 5, 6, 7]:
            self.writing_ship = 'кораблей'
        elif len(self.board.ships.set_list_ships) == 1:
            self.writing_ship = 'корабль'
        elif len(self.board.ships.set_list_ships) in [2, 3, 4]:
            self.writing_ship = 'корабля'

        # print(self.writing_ship)
        return self.writing_ship



class PC(Players):

    def ask (self):
        x_pc = random.randint(0,5)
        y_pc = random.randint(0, 5)
        print(f"Ход компьютера: {x_pc+1} {y_pc+1}")
        return x_pc, y_pc


class User(Players):

    def ask(self):
        while True:
            cords = input("Ваш ход (x - строка, y - столбец): ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print("Введите числа! ")
                continue
            x, y = int(x)-1, int(y)-1
            return x, y


class Game:
    def __init__(self):
        self.us = User()
        self.pc = PC()

    def greet(self):
        print('┌──────────────────────────────────────┐')
        print('│           Добро пожаловать           │')
        print('│                в игру                │')
        print('│             МОРСКОЙ БОЙ              │')
        print('├──────────────────────────────────────┤')
        print('│          формат ввода: x у           │')
        print('│          x - номер строки            │')
        print('│          у - номер столбца           │')
        print('└──────────────────────────────────────┘')

    def loop(self):
        num = 0
        while True:
            print(self.us)
            print(self.pc)

            if num == 0:
                if self.pc.board.shoot(self.us.ask()): # запрашиваем выстрел и проверяем на попадание
                    num = 0
                    if len(self.pc.board.ships.set_list_ships) == 0:
                        print('\033[34m***Победил Игрок!***')
                        break
                    continue
                num = 1

            if num == 1: # Ход Игрока
                if self.us.board.shoot(self.pc.ask()): # запрашиваем выстрел и проверяем на попадание
                    num = 1
                    if len(self.us.board.ships.set_list_ships) == 0:
                        print('\033[34m***Победил Компьютер!***')
                        break
                    continue
                num = 0


    def start(self): # начало игры
        self.greet()
        self.loop()


if __name__ == '__main__':
    g = Game()
    g.start()






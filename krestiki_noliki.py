print("Добро пожаловать в игру крестики - нолики!")
print("Игровое поле имеет размер 3х3. Введите ваш ход в формате")
print("'позиция по горизонтали, позиция по вертикали'")
print("без пробелов и иных символов. Например: 11, 12, 33 и т. д.")

# определение игрового поля
array = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# определение условия выигрыша
win1 = ['X', 'X', 'X']
win2 = ['0', '0', '0']

# определение пустого списка, в этот список помещаются комбинации ходов
line_all = ['', '', '', '', '', '', '', '']

# вывод игрового поля в консоль
def pr():
    for i in range(3):
        for j in range(3):
            print(array[i][j], end="\t")
        print()

# ход игрока "Х", проверка позиции и диапазона ввода
def player1():
    p1 = input("Ходит игрок 'X': ")
    x1 = int(p1[0]) - 1
    y1 = int(p1[1]) - 1
    if (0 <= x1 <= 2) and (0 <= y1 <= 2):
        if array[x1][y1] == '-':
            array[x1][y1] = 'X'
            pr()
        else:
            print("Это значение уже введено")
            player1()
    else:
        print("Введеные цыфры должны быть в интервале от 1 до 3")
        player1()
    var()

# ход игрока "0", проверка позиции и диапазона ввода
def player2():
    p2 = input("Ходит игрок '0': ")
    x2 = int(p2[0]) - 1
    y2 = int(p2[1]) - 1
    if (0 <= x2 <= 2) and (0 <= y2 <= 2):
        if array[x2][y2] == '-':
            array[x2][y2] = '0'
            pr()
        else:
            print("Это значение уже введено")
            player2()
    else:
        print("Введеные цыфры должны быть в интервале от 1 до 3")
        player1()
    var()

# проверка выигрыша
def win_chek():
    if win1 in line_all:
        print('Игра завершена, выиграл игрок "X"!')
        return False
    elif win2 in line_all:
        print('Игра завершена, выиграл игрок "0"!')
        return False
    else:
        return True

# ходы игроков помещаются в списки для проверки выигрыша
def var():
    global line_all
    line1 = [array[0][0], array[1][1], array[2][2]]
    line2 = [array[0][2], array[1][1], array[2][0]]
    line3 = [array[0][0], array[0][1], array[0][2]]
    line4 = [array[1][0], array[1][1], array[1][2]]
    line5 = [array[2][0], array[2][1], array[2][2]]
    line6 = [array[0][0], array[1][0], array[2][0]]
    line7 = [array[0][1], array[1][1], array[2][1]]
    line8 = [array[0][2], array[1][2], array[2][2]]
    line_all = [line1, line2, line3, line4, line5, line6, line7, line8]

# ходы игроков и вызов проверки выигрыша
def game():
    while True:
        if win_chek():
            player1()
        else:
            break
        if win_chek():
            player2()
        else:
            break

game()




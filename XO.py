def chek_winner():
    if arena[0][0] == 'X' and arena[0][1] == 'X' and arena[0][2] == 'X':
        return 'X'
    if arena[1][0] == 'X' and arena[1][1] == 'X' and arena[1][2] == 'X':
        return 'X'
    if arena[2][0] == 'X' and arena[2][1] == 'X' and arena[2][2] == 'X':
        return 'X'
    if arena[0][0] == 'X' and arena[1][0] == 'X' and arena[2][0] == 'X':
        return 'X'
    if arena[0][1] == 'X' and arena[1][1] == 'X' and arena[2][1] == 'X':
        return 'X'
    if arena[0][2] == 'X' and arena[1][2] == 'X' and arena[2][2] == 'X':
        return 'X'
    if arena[0][0] == 'X' and arena[1][1] == 'X' and arena[2][2] == 'X':
        return 'X'
    if arena[0][2] == 'X' and arena[1][1] == 'X' and arena[2][0] == 'X':
        return 'X'

    if arena[0][0] == '0' and arena[0][1] == '0' and arena[0][2] == '0':
        return '0'
    if arena[1][0] == '0' and arena[1][1] == '0' and arena[1][2] == '0':
        return '0'
    if arena[2][0] == '0' and arena[2][1] == 'X' and arena[2][2] == 'X':
        return '0'
    if arena[0][0] == '0' and arena[1][0] == '0' and arena[2][0] == '0':
        return '0'
    if arena[0][1] == '0' and arena[1][1] == '0' and arena[2][1] == '0':
        return '0'
    if arena[0][2] == '0' and arena[1][2] == '0' and arena[2][2] == '0':
        return '0'
    if arena[0][0] == '0' and arena[1][1] == '0' and arena[2][2] == '0':
        return '0'
    if arena[0][2] == '0' and arena[1][1] == '0' and arena[2][0] == '0':
        return '0'
    return '*'

def drow_arena():
    for i in arena:
        print(*i)
    print()

arena = ['*','*','*'],['*','*','*'],['*','*','*']
drow_arena()



for turn in range(1,10):
    print(f'Ход:{turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = int(input(('Введите номер стороки (1,2,3)'))) - 1
    column = int(input(('ведите номер столбца (1,2,3)'))) - 1
    arena[row][column] = turn_char
    drow_arena()

    if arena[row][column] == '*':
        arena[row][column] = turn_char
    else:
        print('Ячейка занята. Пропустите ход.')
        drow_arena()
        continue

    drow_arena

    if chek_winner() == 'X':
        print('Победили крестики!!!')
        break
    if chek_winner() == '0':
        print('Победили нолики!!!')
        break

    if chek_winner() == '*' and turn == 9:
        print('Ничья!!!')




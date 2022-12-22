'''
Создайте программу для игры в "Крестики-нолики".
'''

cell = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def board(cell):
    print(' -----------')
    for i in range(3):
        print('|', cell[0 + i*3], '|', cell[1 + i*3], '|',  cell[2 + i*3], '|')
        print(' -----------')
# print(board(cell))
# my_list = []

def s_input(symb):
    valid = False
    while not valid:
        turn = input('Куда поставить' + symb + '? ')
        try:
            turn = int(turn)
        except:
            print('Некорректный ввод')
            continue
        if 9 >= turn >= 1:
            if (str(cell[turn-1]) not in 'X0'):
                cell[turn-1] = symb
                valid = True
            else:
                print('Указанная позиция занята.')
        else:
            print('Некорректный ввод')
def win_c(cell):
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_comb:
        if cell[i[0]] == cell[i[1]] == cell[i[2]]:
            return cell[i[0]]
    return False

def main(cell):
    count = 0
    win = False

    while not win:
        board(cell)
        if count % 2 == 0:
            s_input('X')
        else:
            s_input('0')
        count += 1
        if count > 4:
            w = win_c(cell)
            if w:
                print(w, 'Победил')
                win = True
                break
        if count == 9:
            print('Ничья')
            break
    board(cell)
main(cell)



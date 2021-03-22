def print_grid():
    print('---------')
    print('|', grid_str[0], grid_str[1], grid_str[2], '|')
    print('|', grid_str[3], grid_str[4], grid_str[5], '|')
    print('|', grid_str[6], grid_str[7], grid_str[8], '|')
    print('---------')

acc_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
grid_str = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print_grid()
X = True
alarm = True

while alarm:
    index = input('Enter the coordinates: ').split()
    if not (index[0] in acc_num and index[1] in acc_num):
        print('You should enter numbers!')
    elif (int(index[0]) > 3 or int(index[1]) > 3 or int(index[0]) < 1 or int(index[1]) < 1):
        print('Coordinates should be from 1 to 3!')
    else:
        index_n = (int(index[0]) - 1) * 3 + int(index[1]) - 1
        if (grid_str[index_n] != ' '):
            print('This cell has occupied! Choose another one!')
        else:
            if X:
                grid_str[index_n] = 'X'
            else:
                grid_str[index_n] = 'O'
            X = not X
            print_grid()
    winx = (grid_str[0] == grid_str[1] == grid_str[2] == 'X') \
           or (grid_str[3] == grid_str[4] == grid_str[5] == 'X') \
           or (grid_str[6] == grid_str[7] == grid_str[8] == 'X') \
           or (grid_str[0] == grid_str[3] == grid_str[6] == 'X') \
           or (grid_str[1] == grid_str[4] == grid_str[7] == 'X') \
           or (grid_str[2] == grid_str[5] == grid_str[8] == 'X') \
           or (grid_str[0] == grid_str[4] == grid_str[8] == 'X') \
           or (grid_str[2] == grid_str[4] == grid_str[6] == 'X')

    wino = (grid_str[0] == grid_str[1] == grid_str[2] == 'O') \
           or (grid_str[3] == grid_str[4] == grid_str[5] == 'O') \
           or (grid_str[6] == grid_str[7] == grid_str[8] == 'O') \
           or (grid_str[0] == grid_str[3] == grid_str[6] == 'O') \
           or (grid_str[1] == grid_str[4] == grid_str[7] == 'O') \
           or (grid_str[2] == grid_str[5] == grid_str[8] == 'O') \
           or (grid_str[0] == grid_str[4] == grid_str[8] == 'O') \
           or (grid_str[2] == grid_str[4] == grid_str[6] == 'O')
    if winx:
        print('X wins')
        alarm = False
    elif wino:
        print('O wins')
        alarm = False
    elif all([i != ' ' for i in grid_str]):
        print('Draw')
        alarm = False

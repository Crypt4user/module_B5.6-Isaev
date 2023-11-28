# игровое поле
board=[1,2,3,4,5,6,7,8,9]
board_scale=3
def print_board():
    print("_" *4* board_scale)
    for i in range(board_scale):
        print((" " * 3 + "|")*3)
        print("",board[i*board_scale], "|", board[1+i*board_scale], "|", board[2+i*board_scale], "|" )
        print(("_"*3 + "|")*3)
def game_step(index, char):
    if index > 9 or index < 1 or board[index-1] in ("X", "0"):
        return False
    board[index-1]= char
    return True
def check_win():
    win = False
    win_combo= ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for pos in win_combo:
        if (board [pos[0]] == board[pos[1]] == board[pos[2]]):
            win = board [pos[0]]
    return win

def start_game():
    current_player = "X"
    step=1
    print_board()
    while (step<10) and (check_win() == False):
        index = int(input ("Ходит игрок "+ current_player + ". Введите номер поля (0 - завершение игры): "))
        if index == 0:
            print("Игра завершена.")
            break
        if game_step(index, current_player):
            print ("Ход выполнен.")
            if current_player == "X":
                current_player = "0"
            else:
                current_player = "X"
            print_board()
            step += 1
        else:
            print ("Недопустимый ход.")
    if step == 10:
        print ("Игра окончена. Ничья.")
    else:
        print("Победил " + check_win())
print("Запуск игры.")
start_game()
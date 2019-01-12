x = "X"
o = "O"
empty = " "
tie = "Ничья"
num_squares = 9


def Start_instruction():
    """ Документирующая инструкция: Вывод правил игры. """
    print(
        """
        Добро пожаловать в игру крестики нолики.Эта игра была создана очень давно.
        Наверное ваши бабушки и дедушки играли в неё.Правила игры очень просты:
        1 - Сначало мы решим кто будет ходить первым(напиши random)
        2 - Потом в порядке очереди вводи число от 0 до 8
        3 - Если 3 клетки по горизонтали, вертикали или диагонали будут 
            заняты одним символом - ПОБЕДА.

            0 | 1 | 2 
            ----------
            3 | 4 | 5 
            ----------
            6 | 7 | 8 
        """)


def ask_number(question, low, high):
    """Ввод диапозона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def ask_yes_no(question):
    """Задает вопрос и принимает ответ да/нет"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def pieces():
    """Определяет 1ый ход и фишки"""
    go_first = ask_yes_no("Хочешь оставить за собой первый ход?(y/n): ")
    if go_first == "y":
        print("Ты ходишь первый, твои фишки - Х.")
        human = x
        computer = o
    else:
        print("Ты ходишь второй, твои фишки - О.")
        human = o
        computer = x
    return computer, human


def new_board():
    """Создает новую игровую доску"""
    board = []
    for square in range(num_squares):
        board.append(empty)
    return board


def display_board(board):
    """Отображает игровую доску на экране"""

    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Создает список доступных ходов"""
    moves = []
    for square in range(num_squares):
        if board[square] == empty:
            moves.append(square)
    return moves


def winner(board):
    """Определяет есть ли победитель"""
    ways_to_win = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner
        if empty not in board:
            return tie
    return None


def human_move(board, human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери одно из полей: ", 0, num_squares)
        if move not in legal:
            print("Поле уже занято.")
    print("Принял.")
    return move


def computer_move(board, computer, human):
    """Делает ход за комьютерного противника"""
    board = board[:]
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)  # polia dlia hoda ot luchshego k hudshemu\
    print("Я выбрал поле номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = empty

    # если компьюютер не может выйграть - он смотрит , может ли выйграть человек

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = empty

    # иначе выполняется следующее

    for move in best_moves:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Переход хода"""
    if turn == x:
        return o
    else:
        return x


def congrat_winner(the_winner):
    """Поздравление победителя"""

    if the_winner != tie:
        print("Победил - %s" % the_winner)
    else:
        print("Ничья.")


def main():
    Start_instruction()  # абстракция - описания действия без подробностей
    # инкапсуляция - упаковка дейсвтий в 1 пакет(звук больше меньше от 1ого к 10ому)
    computer, human = pieces()
    turn = x
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        print(board)
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner)


main()
print("\n Нажмите Enter,чтобы выйти.")

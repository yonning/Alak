def alak():
    # variables
    user_input = False
    while not user_input:
        try:
            n = int(input('Enter a number of square to start the game : n = '))
            while n < 3:
                print('Enter a bigger number of square to start')
                n = int(input('Enter a number of square to start the game : n = '))
            user_input = True
        except ValueError:
            print('Invalid input! Please try again with exclusively a number.')
    pieces = ['.', 'X', 'O']
    board = []
    place = []
    removed = []

    new_board(n, pieces, board)
    numbers(n, place)
    display(board, place)
    graveyard(n, pieces, removed)
    state = False
    turn = 0
    while state is False:
        if turn % 2 == 0:
            player = 1
            print('\n')
            print('Player 1 (X)')
            select(n, pieces, board, removed, player)
            display(board, place)
            state = win(board, n, pieces, removed)
        else:
            player = 2
            print('\n')
            print('Player 2 (O)')
            select(n, pieces, board, removed, player)
            display(board, place)
            state = win(board, n, pieces, removed)
        turn += 1


def new_board(n, pieces, board):
    for a in range(0, n):
        board.append(pieces[0])
    return board


def numbers(n, place):
    for b in range(1, n + 1):
        place.append(b)
    return place


def display(board, place):
    print('\n')
    print(*board, sep=' ')
    print(*place, sep=' ')


def graveyard(n, pieces, removed):
    for a in range(0, n):
        removed.append(pieces[0])


def clear_graveyard(removed):
    for a, b in enumerate(removed):
        if b == 'X':
            removed[a] = '.'
        if b == 'O':
            removed[a] = '.'


def possible(i, n, pieces, board, removed):
    if i > n:
        return True
    elif board[i - 1] == pieces[1]:
        return True
    elif board[i - 1] == pieces[2]:
        return True
    elif removed[i - 1] == pieces[1]:
        return True
    elif removed[i - 1] == pieces[2]:
        return True
    else:
        return False


def select(n, pieces, board, removed, player):
    user = False
    while not user:
        try:
            i = int(input('Choose a licit number of square: '))
            user = True
        except ValueError:
            print('ERROR ! No Input detected.')
    again = possible(i, n, pieces, board, removed)
    while again is True:
        i = int(input('Choose a licit number of square: '))
        again = possible(i, n, pieces, board, removed)
    put(board, n, player, removed, i, pieces)


def put(board, n, player, removed, i, pieces):
    if player == 1:
        board[i - 1] = pieces[1]
    if player == 2:
        board[i - 1] = pieces[2]
    clear_graveyard(removed)
    capture(board, removed, player, i, n)


def capture(board, removed, player, i, n):
    x = i - 1
    if player == 1:
        take = False
        for c in range(x - 1, -1, -1):
            if board[c] == 'X':
                take = True
                break
            if board[c] == 'O':
                take = True
            elif board[c] == '.':
                take = False
                break
        if take is True:
            try:
                for d in range(x - 1, c - 1, -1):
                    if board[d] == 'O':
                        board[d] = '.'
                        removed[d] = 'O'
                    else:
                        board[d] = 'X'
            except UnboundLocalError:
                board = board
        for a in range(x + 1, n + 1):
            try:
                if board[a] == 'X':
                    take = True
                    break
                elif board[a] == 'O':
                    take = True
                elif board[a] == '.':
                    take = False
                    break
            except IndexError:
                pass

        if take is True:
            try:
                for d in range(x + 1, a):
                    if board[d] == 'O':
                        board[d] = '.'
                        removed[d] = 'O'
                    else:
                        board[d] = 'X'
            except UnboundLocalError:
                board = board

    if player == 2:
        take = False
        for c in range(x - 1, -1, -1):
            if board[c] == 'O':
                take = True
                break
            if board[c] == 'X':
                take = True
            elif board[c] == '.':
                take = False
                break
        if take is True:
            try:
                for d in range(x - 1, c - 1, -1):
                    if board[d] == 'X':
                        board[d] = '.'
                        removed[d] = 'X'
                    else:
                        board[d] = 'O'
            except UnboundLocalError:
                board = board
        for a in range(x + 1, n + 1):
            try:
                if board[a] == 'O':
                    take = True
                    break
                elif board[a] == 'X':
                    take = True
                elif board[a] == '.':
                    take = False
                    break
            except IndexError:
                pass

        if take is True:
            try:
                for d in range(x + 1, a):
                    if board[d] == 'X':
                        board[d] = '.'
                        removed[d] = 'O'
                    else:
                        board[d] = 'O'
            except UnboundLocalError:
                board = board

                
def win(board, n, pieces, removed):
    play = 0
    for i in range(n):
        z = not possible(i, n, pieces, board, removed)
        if z is True:
            play += 1
    if play == 0:
        p1 = board.count('X')
        p2 = board.count('O')
        if p1 > p2:
            print('Winner is Player 1')
            return True
        elif p1 < p2:
            print('Winner is Player 2')
            return True
        else:
            print('Equality')
            return True
    else:
        return False


alak()

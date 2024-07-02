def boarding_passengers(capacity, *args):
    board = {}
    check_capacity = 0

    for boarding_info in args:
        if boarding_info[1] not in board:
            board[boarding_info[1]] = boarding_info[0]
        else:
            board[boarding_info[1]] += boarding_info[0]



print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))











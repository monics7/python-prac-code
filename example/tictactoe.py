game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(player=0, row=0, col=0, just_display=False):
    if not just_display:
        game[row][col] = player
    print("   a  b  c")
    for count, row in enumerate(game):
        print(count, row)


game_board(1, 2, 0)

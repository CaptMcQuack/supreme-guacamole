p1 = input('Player 1 please choose (x) or (O): ')
winner = ''
if p1.upper() == 'X':
    p2 = 'O'
else:
    p2 = 'X'

arr = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

row, col = 0, 0

total = 0
win = False

for x in range(1, 10):
    total = 0
    if (x % 2) != 0:
        if not win:
            player_1_I = input('Player 1 please choose a coordinate: ')
            i_index = player_1_I.index(',')
            z = slice(0, 1)
            y = slice(i_index + 1, i_index + 2)
            row = int(player_1_I[z])
            col = int(player_1_I[y])
            while (row > 2) or (col > 2):
                print('That coordinate is too large!')
                player_1_I = input('Player 1 please choose a coordinate: ')
                i_index = player_1_I.index(',')
                z = slice(0, 1)
                y = slice(i_index + 1, i_index + 2)
                row = int(player_1_I[z])
                col = int(player_1_I[y])
            else:
                while arr[row][col] != '*':
                    print('That coordinate has already been played!')
                    player_1_I = input('Player 1 please choose a coordinate: ')
                    i_index = player_1_I.index(',')
                    z = slice(0, 1)
                    y = slice(i_index + 1, i_index + 2)
                    row = int(player_1_I[z])
                    col = int(player_1_I[y])
                else:
                    arr[row][col] = p1
                    for k in range(3):
                        print(arr[k])

                    total = 0
                    for y in range(3):
                        if arr[y][0] == p1:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p1'
                                break

                    total = 0
                    for y in range(3):
                        if arr[y][1] == p1:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p1'
                                break

                    total = 0
                    for y in range(3):
                        if arr[y][2] == p1:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p1'
                                break

                    total = 0
                    for y in range(3):
                        if arr[0][y] == p1:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p1'
                                break

                    total = 0
                    for y in range(3):
                        if arr[1][y] == p1:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p1'
                                break

                    total = 0
                    for y in range(3):
                        if arr[2][y] == p1:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p1'
                                break

                    total = 0
                    for y in range(3):
                        if arr[y][y] == p1:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p1'
                                break

                    count_1, count_2 = 2, 0
                    total = 0
                    for y in range(3):
                        if arr[count_1][count_2] == p1:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p1'
                                break
                        count_1 -= 1
                        count_2 += 1

    else:
        if not win:
            player_2_I = input('Player 2 please choose a coordinate: ')
            i_index = player_2_I.index(',')
            z = slice(0, 1)
            y = slice(i_index + 1, i_index + 2)
            row = int(player_2_I[z])
            col = int(player_2_I[y])
            while (row > 2) or (col > 2):
                print('That coordinate is too large!')
                player_2_I = input('Player 2 please choose a coordinate: ')
                i_index = player_2_I.index(',')
                z = slice(0, 1)
                y = slice(i_index + 1, i_index + 2)
                row = int(player_2_I[z])
                col = int(player_2_I[y])
            else:
                while arr[row][col] != '*':
                    print('That coordinate has already been played!')
                    player_2_I = input('Player 2 please choose a coordinate: ')
                    i_index = player_2_I.index(',')
                    z = slice(0, 1)
                    y = slice(i_index + 1, i_index + 2)
                    row = int(player_2_I[z])
                    col = int(player_2_I[y])
                else:
                    arr[row][col] = p2
                    for k in range(3):
                        print(arr[k])

                    total = 0
                    for y in range(3):
                        if arr[y][0] == p2:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p2'
                                break

                    total = 0
                    for y in range(3):
                        if arr[y][1] == p2:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p2'
                                break

                    total = 0
                    for y in range(3):
                        if arr[y][2] == p2:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p2'
                                break

                    total = 0
                    for y in range(3):
                        if arr[0][y] == p2:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p2'
                                break

                    total = 0
                    for y in range(3):
                        if arr[1][y] == p2:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p2'
                                break

                    total = 0
                    for y in range(3):
                        if arr[2][y] == p2:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p2'
                                break

                    total = 0
                    for y in range(3):
                        if arr[y][y] == p2:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p2'
                                break

                    count_1, count_2 = 2, 0
                    total = 0
                    for y in range(3):
                        if arr[count_1][count_2] == p2:
                            total += 1
                            if total == 3:
                                win = True
                                winner = 'p2'
                                break
                        count_1 -= 1
                        count_2 += 1

    if winner == 'p1':
        print('Player 1 won!')
        break
    elif winner == 'p2':
        print('Player 2 won!')
        break
    elif x == 9:
        print("It's a draw!")

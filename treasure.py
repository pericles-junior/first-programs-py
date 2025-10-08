board = [ [' ' for _ in range(3)] for _ in range(3)]

line_treasure = 1
column_treasure = 2
def showBoard():
    for line in board:
        print('|'.join(line))
        print('-' * 5)

attempts = 5

print('🚀 Space Treasure Hunt')
print('Find the 💎  hidden in the 3x3 board.')
print('Use numbers between 0 and 2 for line and column.')
print('Example: line 0, column 2')

for i in range(attempts):
    print(f'\nAttempt {i+1} of {attempts}')

    line = int(input('Type the line (0 to 2): '))
    column = int(input('Type the column (0 to 2): '))

    if line < 0 or line > 2 or column < 0 or column > 2:
        print('❌ Invalid position! Try values numbers between 0 and 2.')
        continue
    
    if line == line_treasure and column == column_treasure:
        board[line][column] = '💎'
        print('\n🎉 Congratulations! You find  the treasure!')
        showBoard()
        break
    else:
        if board[line][column] != ' ':
            print('⚠️ You tried here!')
        else:
            board[line][column] = 'X'
            print('Nothing here... Keep trying.')
        showBoard()
else:
    print('\n⛔ Your attempts are over!')
    board[line_treasure][column_treasure] = '💎'
    print('The treasure was here:')
    showBoard()
import streamlit as st
st.code('''def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_win(board, player_symbol):
    for i in range(3):
        if all(cell == player_symbol for cell in board[i]):  # Check rows
            return True
        if all(board[j][i] == player_symbol for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player_symbol for i in range(3)):  # Check main diagonal
        return True
    if all(board[i][2 - i] == player_symbol for i in range(3)):  # Check secondary diagonal
        return True
    return False

game_board = [["","",""],
              ["","",""],
              ["","",""]]
print_board(game_board)
    
counter = 0
while counter < 9:
    player_symbol = 'x' if counter % 2 == 0 else 'o'
    print(f"Player-{player_symbol.upper()}'s turn:\n")
        
    while True:
        r, c = map(int, input("Enter row and column in range (0-2), separated by space:\n").split())
        if 0 <= r < 3 and 0 <= c < 3 and game_board[r][c] == '':
            game_board[r][c] = player_symbol
            break
        else:
            print("You Can't Write On This Grid!\n")
        
    print_board(game_board)
        
    if check_win(game_board, player_symbol):
        print(f"Player {player_symbol.upper()} has won!")
        break
        
    counter += 1
    
if counter == 9:
    print("It's a tie!")''',language='python')
class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # Player starts

    def print_board(self):
        print("\nTic Tac Toe Board:")
        for i, row in enumerate(self.board):
            print(" " + " | ".join(row))
            if i < len(self.board) - 1:
                print("---+---+---")
        print()

    def is_winner(self, player):
        win_conditions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]],
        ]
        return [player, player, player] in win_conditions

    def is_board_full(self):
        return all(all(cell != " " for cell in row) for row in self.board)

    def make_move(self, row, col, player):
        if self.board[row][col] == " ":
            self.board[row][col] = player
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def minimax(self, board, depth, is_maximizing):
        if self.is_winner("O"):
            return 1
        if self.is_winner("X"):
            return -1
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = " "
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        score  = self.minimax(board, depth + 1, True)
                        board[i][j] = " " 
                        best_score = min(best_score, score)
            return best_score
            


    def find_best_move(self):
        # Find best move for AI (computer)
        best_move = None
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j]
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def get_player_input(self):
        valid_input = False
        while not valid_input:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and self.board[row][col] == " ":
                    valid_input = True
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a valid number between 0 and 2.")
        return row, col

    def play_game(self):
        while not self.is_board_full():
            self.print_board()
            if self.current_player == "X":
                print("Player X's turn.")
                row, col = self.get_player_input()
                self.make_move(row, col, "X")
                if self.is_winner("X"):
                    print("Congratulations! Player X wins!")
                    break
            else:
                print("Computer (O) is making a move...")
                row, col = self.find_best_move()
                self.make_move(row, col, "O")
                if self.is_winner("O"):
                    print("Computer (O) wins! Better luck next time.")
                    break

            self.switch_player()

        self.print_board()
        if not self.is_winner("X") and not self.is_winner("O"):
            print("It's a draw! Well played both!")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

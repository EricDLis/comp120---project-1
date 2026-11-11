Tic-Tac-Toe vs. the Computer

This is a C program where you play tic-tac-toe against the computer in the terminal. It is Project 1 for COMP 120.

How to run

Compile the program with gcc tictactoe.c -o tictactoe, then start it with ./tictactoe.

How to play

You are O and you always go first. The computer is X. The squares on the board are numbered 0 to 8

On your turn, type the number of an empty square and press Enter. You win by getting three of your symbols in a row, going across, down, or diagonally. If all 9 squares are full and nobody has won, the game is a draw. After each game, type y to play again or q to quit.

What the program does

The board is stored in a 1-D char array of 9 elements, and an empty square is a space. When the board is shown, each empty square displays its own number, so you always know which squares are still open.

The computer picks random empty squares using rand(). It is not a smart player, but it always makes a legal move. The program calls srand() once at the start so every run is different.

The program checks for bad input and asks again. It handles a number outside 0 to 8, a square that is already taken, and text that is not a number. When the game ends, it tells you whether you won, the computer won, or it was a draw.

How the code is organized

The program is split into small functions that each do one job. init_board sets all 9 squares to empty. display_board prints the board and uses a temporary array named c to show the numbers of the empty squares. is_winner returns true if a player has three in a row. other_player returns the opposite symbol.

get_human_move keeps asking until the user enters a valid empty square. get_computer_move picks a random empty square. take_turn lets the current player make one move. play_game plays one full game, and play_again asks whether to play another one. The main function calls srand(), prints the title, and repeats play_game for as long as the user wants to keep playing.

Concepts used

This project uses variables, char arrays, bool, if, for, while, do...while, user-defined functions, rand(), and srand().

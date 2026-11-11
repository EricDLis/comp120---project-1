#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

// Set all 9 squares to empty
void init_board(char board[]) {
    for (int i = 0; i < 9; ++i) {
        board[i] = ' ';
    }
}

// Print the board. Empty squares show their number.
void display_board(char board[]) {
    char c[9];
    for (int i = 0; i < 9; ++i) {
        c[i] = board[i];
        if (board[i] == ' ') c[i] = '0' + i;
    }
    printf("\n %c | %c | %c\n---+---+---\n %c | %c | %c\n---+---+---\n %c | %c | %c\n\n",
           c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8]);
}

// True if player p has three in a row (rows, columns, diagonals)
bool is_winner(char b[], char p) {
    return (b[0] == p && b[1] == p && b[2] == p) || (b[3] == p && b[4] == p && b[5] == p) || (b[6] == p && b[7] == p && b[8] == p) ||
           (b[0] == p && b[3] == p && b[6] == p) || (b[1] == p && b[4] == p && b[7] == p) || (b[2] == p && b[5] == p && b[8] == p) ||
           (b[0] == p && b[4] == p && b[8] == p) || (b[2] == p && b[4] == p && b[6] == p);
}

// Return the other player's symbol
char other_player(char p) {
    if (p == 'O') return 'X';
    return 'O';
}

// Ask until the user types a valid empty square
int get_human_move(char board[]) {
    char line[50];
    int square = 0;
    bool valid = false;
    while (!valid) {
        printf("Your turn (O). Enter a square number (0-8): ");
        fgets(line, sizeof(line), stdin);
        square = line[0] - '0';
        if (line[0] < '0' || line[0] > '8' || line[1] != '\n') printf("  Please type one number from 0 to 8.\n");
        else if (board[square] != ' ') printf("  That square is already taken. Choose an empty one.\n");
        else valid = true;
    }
    return square;
}

// Pick random squares until one is empty
int get_computer_move(char board[]) {
    int square;
    do {
        square = rand() % 9;
    } while (board[square] != ' ');
    return square;
}

// Let one player make one move
void take_turn(char board[], char player) {
    int square;
    if (player == 'O') {
        square = get_human_move(board);
    }
    else {
        printf("Computer (X) is thinking...\n");
        square = get_computer_move(board);
        printf("Computer (X) chose square %d.\n", square);
    }
    board[square] = player;
}

// Play one full game
void play_game(void) {
    char board[9];
    char player = 'O';
    bool game_over = false;

    init_board(board);
    display_board(board);

    for (int turn = 0; turn < 9 && !game_over; ++turn) {
        take_turn(board, player);
        display_board(board);
        if (is_winner(board, player)) {
            if (player == 'O') printf("You (O) win! Great job!\n");
            else printf("The computer (X) wins. Better luck next time!\n");
            game_over = true;
        }
        else {
            player = other_player(player);
            if (player == 'O') printf("Your move next!\n");
        }
    }

    if (!game_over) printf("It's a draw!\n");
}

// Ask y or q until the answer is valid
bool play_again(void) {
    char line[50];
    bool valid = false;
    while (!valid) {
        printf("\nPlay again (y) or quit (q)? ");
        fgets(line, sizeof(line), stdin);
        if (line[0] == 'y' || line[0] == 'Y' || line[0] == 'q' || line[0] == 'Q') valid = true;
        else printf("  Please type y or q.\n");
    }
    return line[0] == 'y' || line[0] == 'Y';
}

int main(void) {
    srand(time(NULL));

    printf("=====================================\n");
    printf("        TIC-TAC-TOE vs COMPUTER\n");
    printf("=====================================\n");
    printf("You are O and you go first. The computer is X.\n");
    printf("On your turn, type the number of an empty square:\n");

    do {
        play_game();
    } while (play_again());

    printf("Thanks for playing!\n");
    return 0;
}

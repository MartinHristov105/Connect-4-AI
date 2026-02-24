from src.constants import *

# We create a 2D numpy matrix of zeros.
def create_board():
    return numpy.zeros((ROW, COLUMN))

# We draw the board using rectangles and circles. 
# Where we have placed a checker, we color it with the corresponding color.
def draw_board(screen, board):
    for col in range(COLUMN):
        for row in range(ROW):
            pygame.draw.rect(screen, GREY, (col * RECT, row * RECT + RECT, RECT, RECT))
            pygame.draw.circle(screen, WHITE, (int(col * RECT + RECT / 2), int(row * RECT + RECT + RECT / 2)), RAD)
    
    for col in range(COLUMN):
        for row in range(ROW):
            if board[row, col] == PLAYER_PIECE:
                pygame.draw.circle(screen, YELLOW, (int(col * RECT + RECT / 2), HEIGHT - int(row * RECT + RECT / 2)), RAD)
            elif board[row, col] == AI_PIECE:
                pygame.draw.circle(screen, BLUE, (int(col * RECT + RECT / 2), HEIGHT - int(row * RECT + RECT / 2)), RAD)
    pygame.display.update()

# We check whether the top row of a belt is free.
def is_loc_free(board, col):
    return board[ROW - 1, col] == EMPTY

# List of indexes of all free columns. 
def get_loc_free(board):
    free_locations = []
    for col in range(COLUMN):
        if is_loc_free(board, col):
            free_locations.append(col)
    return free_locations

# Drop a checker.
def drop_piece(board, row, col, player):
    board[row, col] = player

# Takes the first free space in the column where we want to place a checker.
def open_row(board, col):
    for row in range(ROW):
        if board[row, col] == EMPTY:
            return row

# Checking for a winning move.
def win_move(board, player):
    # Вертикално
    for col in range(COLUMN):
        for row in range(ROW - 3):
            if board[row, col] == board[row + 1, col] == board[row + 2, col] == board[row + 3, col] == player:
                return True
    
    # Horizontally.
    for row in range(ROW):
        for col in range(COLUMN - 3):
            if board[row, col] == board[row, col + 1] == board[row, col + 2] == board[row, col + 3] == player:
                return True

    # Top-left, bottom-right.   
    for row in range(ROW - 3):
        for col in range(COLUMN - 3):
            if board[row, col] == board[row + 1, col + 1] == board[row + 2, col + 2] == board[row + 3, col + 3] == player:
                return True

    # Bottom-left, top-right.    
    for row in range(ROW - 1, 2 , -1):
        for col in range(COLUMN - 3):
            if board[row, col] == board[row - 1, col + 1] == board[row - 2, col + 2] == board[row - 3, col + 3] == player:
                return True
    return False

# Checks if there is an empty space on the board. From 2D -> 1D array.
def full_board(board):
    return sum(board.flatten() == 0) == 0